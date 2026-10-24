"""Validate the local package invariants; never contact the Spine endpoint.

Run: uv run --no-project --with jsonschema scripts/validate.py
Only the two official Agent Plugins JSON Schemas are downloaded.
"""

import json
from pathlib import Path
from urllib.request import urlopen

from jsonschema.validators import validator_for


ROOT = Path(__file__).resolve().parents[1]
ENDPOINT = "https://app.spine-kb.com/mcp"
PACKAGES = ("spine-openai", "spine-claude", "spine-antigravity")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def contained_path(root, value):
    require(value.startswith("./"), f"Expected a relative ./ path: {value}")
    path = (root / value).resolve()
    require(path.is_relative_to(root.resolve()), f"Path escapes its root: {value}")
    require(path.exists(), f"Missing path: {value}")
    return path


def main():
    json_files = sorted(ROOT.rglob("*.json"))
    parsed = {path: read_json(path) for path in json_files}
    require(len(parsed) == 8, "Unexpected JSON file set; review validation coverage")
    require(not list(ROOT.rglob(".app.json")), "Account app mappings are out of scope")

    portable_root = ROOT / "plugins/spine-openai"
    for filename in ("plugin.json", "mcp.json"):
        data = parsed[portable_root / filename]
        schema_url = data["$schema"]
        expected = f"https://agent-plugins.org/schemas/1.0.0/{filename.removesuffix('.json')}.schema.json"
        require(schema_url == expected, f"Unexpected schema URL: {schema_url}")
        with urlopen(schema_url, timeout=20) as response:
            schema = json.load(response)
        validator = validator_for(schema)
        validator.check_schema(schema)
        validator(schema).validate(data)
        print(f"Schema passed: {filename} ({schema_url})")

    source = (ROOT / "bootstrap/spine/SKILL.md").read_bytes()
    for package in PACKAGES:
        package_root = ROOT / "plugins" / package
        skill = contained_path(package_root, "./skills/spine/SKILL.md")
        require(skill.read_bytes() == source, f"Bootstrap copy differs: {package}")
        manifest_path = package_root / (
            ".claude-plugin/plugin.json" if package == "spine-claude" else "plugin.json"
        )
        manifest = parsed[manifest_path]
        require(manifest["name"] == package, f"Wrong plugin identity: {package}")
        if package == "spine-antigravity":
            require(
                set(manifest) == {"name", "description"},
                "Review Antigravity manifest against the current official docs",
            )
            config = parsed[package_root / "mcp_config.json"]
            expected = {"mcpServers": {"spine": {"serverUrl": ENDPOINT}}}
        else:
            require(
                manifest["author"]["name"] == "SpineDev",
                f"Wrong plugin author: {package}",
            )
            if package == "spine-openai":
                interface = manifest["extensions"]["com.openai"]["interface"]
                require(interface["developerName"] == "SpineDev", "Wrong OpenAI developer")
                icon_paths = (interface["composerIcon"], interface["logo"])
            else:
                icon_paths = (manifest["icon"],)
            for icon_path in icon_paths:
                require(
                    contained_path(package_root, icon_path).is_file(),
                    f"Icon is not a file: {package}/{icon_path}",
                )
            filename = ".mcp.json" if package == "spine-claude" else "mcp.json"
            config = dict(parsed[package_root / filename])
            config.pop("$schema", None)
            transport = "http" if package == "spine-claude" else "streamable-http"
            expected = {"mcpServers": {"spine": {"type": transport, "url": ENDPOINT}}}
        require(config == expected, f"Unexpected MCP fields or endpoint: {package}")

    for relative_path, package in (
        (".agents/plugins/marketplace.json", "spine-openai"),
        (".claude-plugin/marketplace.json", "spine-claude"),
    ):
        catalog = parsed[ROOT / relative_path]
        require(len(catalog["plugins"]) == 1, f"Unexpected entries: {relative_path}")
        entry = catalog["plugins"][0]
        require(entry["name"] == package, f"Wrong catalog target: {relative_path}")
        source_ref = entry["source"]
        if isinstance(source_ref, dict):
            require(source_ref["source"] == "local", "Catalog requires local sources")
            source_ref = source_ref["path"]
            require(
                entry["policy"] == {
                    "installation": "AVAILABLE",
                    "authentication": "ON_INSTALL",
                }
                and entry["category"] == "Productivity",
                "Unexpected OpenAI catalog policy",
            )
        else:
            require(catalog["owner"]["name"] == "SpineDev", "Wrong catalog owner")
        require(
            contained_path(ROOT, source_ref) == ROOT / "plugins" / package,
            f"Catalog resolves to the wrong package: {relative_path}",
        )

    print("Passed: 8 JSON files, 3 MCP adapters, 2 catalogs, 4 identical skills")
    print("Only schema endpoints were contacted; clients and Spine were not used")


if __name__ == "__main__":
    main()
