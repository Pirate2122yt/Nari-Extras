"""Update Nari-Extras README badges and downloads from its versioned plugin ZIPs."""
import argparse
from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
from urllib.parse import quote
from zipfile import ZipFile


VERSION = r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)"


@dataclass(frozen=True)
class Plugin:
    folder: str
    prefix: str
    id: str
    name: str
    badge: str
    color: str
    dot: str
    description: str


PLUGINS = (
    Plugin("Listening-Wrapped", "listening-wrapped", "listening_wrapped", "Listening Wrapped", "Listening_Wrapped", "ed4963", "🔴", "Your month or year in music, with top songs, artists, albums, and listening time."),
    Plugin("Queue-Tools", "queue-tools", "queue_tools", "Queue Tools", "Queue_Tools", "4cba7b", "🟢", "Remove duplicates, shuffle upcoming songs, and choose how many songs each artist gets."),
    Plugin("Source-Switcher", "source-switcher", "source_switcher", "Quick Source Switcher", "Source_Switcher", "009ff3", "🔵", "Choose your music sources and switch between them with a corner button."),
)


def latest(root, plugin):
    folder = root / "Plugins" / plugin.folder
    pattern = re.compile(re.escape(plugin.prefix) + rf"-({VERSION})\.zip")
    candidates = []
    for path in folder.glob("*.zip"):
        match = pattern.fullmatch(path.name)
        if match:
            candidates.append((tuple(map(int, match[1].split("."))), match[1], path))
    if not candidates:
        raise ValueError(f"No stable {plugin.prefix}-X.Y.Z.zip found in {folder}")
    _, version, path = max(candidates)
    with ZipFile(path) as archive:
        info = archive.getinfo("manifest.json")
        if info.file_size > 65536:
            raise ValueError(f"Manifest is too large: {path.name}")
        manifest = json.loads(archive.read(info))
    if manifest.get("id") != plugin.id or manifest.get("version") != version:
        raise ValueError(f"ZIP name and manifest do not match: {path.name}")
    return version, path.relative_to(root).as_posix()


def replace_section(text, key, content, original_pattern):
    start, end = f"<!-- {key}:start -->", f"<!-- {key}:end -->"
    block = start + "\n" + content.rstrip() + "\n" + end
    if start in text or end in text:
        if text.count(start) != 1 or text.count(end) != 1 or text.index(start) >= text.index(end):
            raise ValueError(f"Invalid README markers for {key}")
        pattern = re.escape(start) + r".*?" + re.escape(end)
    else:
        # First run recognizes the current public README. Later runs only
        # rewrite these marked sections, keeping the rest of the page intact.
        pattern = original_pattern
    result, count = re.subn(pattern, lambda _: block, text, flags=re.M | re.S)
    if count != 1:
        raise ValueError(f"Could not find exactly one {key} section in README.md")
    return result


def render(text, releases, repository):
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise ValueError("Repository must be owner/name")
    base = f"https://github.com/{repository}"
    badges = []
    rows = ["| Plugin | What it does | Download |", "| :--- | :--- | :---: |"]
    for plugin, (version, filename) in zip(PLUGINS, releases, strict=True):
        folder = f"{base}/tree/main/Plugins/{quote(plugin.folder)}"
        download = f"{base}/raw/refs/heads/main/{quote(filename, safe='/')}"
        badge_name = plugin.name.removeprefix("Quick ")
        badges.append(f"[![{badge_name} {version}](https://img.shields.io/badge/{plugin.badge}-{version}-{plugin.color}?style=for-the-badge)]({folder})")
        rows.append(f"| {plugin.dot} **[{plugin.name}]({folder})** | {plugin.description} | [**v{version} · ZIP**]({download}) |")
    badge_pattern = r"^\[!\[Listening Wrapped [^\n]+\n\[!\[Queue Tools [^\n]+\n\[!\[Source Switcher [^\n]+"
    table_pattern = r"^\| Plugin \| What it does \| Download \|\n(?:\|[^\n]*(?:\n|$))+"
    text = replace_section(text, "plugin-badges", "\n".join(badges), badge_pattern)
    return replace_section(text, "plugin-downloads", "\n".join(rows), table_pattern)


def update(root, repository="Pirate2122yt/Nari-Extras"):
    path = root / "README.md"
    before = path.read_text(encoding="utf-8")
    releases = [latest(root, plugin) for plugin in PLUGINS]
    after = render(before, releases, repository)
    if before == after:
        return False
    path.write_text(after, encoding="utf-8")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--repository", default=os.environ.get("GITHUB_REPOSITORY", "Pirate2122yt/Nari-Extras"))
    args = parser.parse_args()
    changed = update(args.root, args.repository)
    print("Updated README download links and badges." if changed else "README is already up to date.")
