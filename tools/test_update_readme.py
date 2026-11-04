import json
from pathlib import Path
import tempfile
import unittest
from zipfile import ZipFile

from update_readme import PLUGINS, latest, update


README = """# My Nari Extras

Keep my custom introduction.

[![Listening Wrapped 1.0.0](https://img.shields.io/badge/Listening_Wrapped-1.0.0-ed4963?style=for-the-badge)](https://github.com/Pirate2122yt/Nari-Extras/tree/main/Plugins/Listening-Wrapped)
[![Queue Tools 1.0.0](https://img.shields.io/badge/Queue_Tools-1.0.0-4cba7b?style=for-the-badge)](https://github.com/Pirate2122yt/Nari-Extras/tree/main/Plugins/Queue-Tools)
[![Source Switcher 1.0.0](https://img.shields.io/badge/Source_Switcher-1.0.0-009ff3?style=for-the-badge)](https://github.com/Pirate2122yt/Nari-Extras/tree/main/Plugins/Source-Switcher)

## The plugins

| Plugin | What it does | Download |
| :--- | :--- | :---: |
| Wrapped | Stats | old link |
| Queue | Queue | old link |
| Sources | Sources | old link |

Keep my installation instructions and credits.
"""


class UpdateReadmeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix=".readme-updater-", dir=Path.cwd())
        self.root = Path(self.temp.name)
        self.assertTrue(self.root.resolve().is_relative_to(Path.cwd().resolve()))
        (self.root / "README.md").write_text(README, encoding="utf-8")
        for plugin in PLUGINS:
            self.add_zip(plugin, "1.0.0")

    def tearDown(self):
        self.temp.cleanup()

    def add_zip(self, plugin, version, manifest_version=None):
        folder = self.root / "Plugins" / plugin.folder
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / f"{plugin.prefix}-{version}.zip"
        with ZipFile(path, "w") as archive:
            archive.writestr("manifest.json", json.dumps({"id": plugin.id, "version": manifest_version or version}))
        return path

    def text(self):
        return (self.root / "README.md").read_text(encoding="utf-8")

    def test_compares_versions_numerically(self):
        plugin = PLUGINS[0]
        self.add_zip(plugin, "1.9.9")
        self.add_zip(plugin, "1.10.0")
        self.assertEqual(latest(self.root, plugin)[0], "1.10.0")

    def test_updates_links_and_badges_without_changing_other_sections(self):
        for plugin, version in zip(PLUGINS, ("1.3.2", "1.0.3", "1.2.3")):
            self.add_zip(plugin, version)
        self.assertTrue(update(self.root))
        text = self.text()
        self.assertIn("Keep my custom introduction.", text)
        self.assertIn("Keep my installation instructions and credits.", text)
        for plugin, version in zip(PLUGINS, ("1.3.2", "1.0.3", "1.2.3")):
            self.assertIn(f"{plugin.prefix}-{version}.zip", text)
            self.assertIn(f"{plugin.badge}-{version}-", text)
        self.assertEqual(text.count("<!-- plugin-badges:start -->"), 1)
        self.assertEqual(text.count("<!-- plugin-downloads:start -->"), 1)

    def test_second_run_is_unchanged(self):
        update(self.root)
        before = self.text()
        self.assertFalse(update(self.root))
        self.assertEqual(before, self.text())

    def test_new_upload_advances_link_and_old_upload_does_not_downgrade(self):
        plugin = PLUGINS[1]
        update(self.root)
        self.add_zip(plugin, "2.0.0")
        self.assertTrue(update(self.root))
        self.add_zip(plugin, "1.5.0")
        self.assertFalse(update(self.root))
        self.assertIn("queue-tools-2.0.0.zip", self.text())

    def test_ignores_prereleases_and_other_file_names(self):
        plugin = PLUGINS[0]
        folder = self.root / "Plugins" / plugin.folder
        (folder / "listening-wrapped-9.0.0-beta.zip").touch()
        (folder / "unrelated-99.0.0.zip").touch()
        self.assertEqual(latest(self.root, plugin)[0], "1.0.0")

    def test_manifest_mismatch_does_not_modify_readme(self):
        self.add_zip(PLUGINS[2], "1.2.3", manifest_version="1.2.2")
        with self.assertRaisesRegex(ValueError, "do not match"):
            update(self.root)
        self.assertEqual(self.text(), README)

    def test_missing_plugin_does_not_modify_readme(self):
        self.add_zip(PLUGINS[2], "1.0.0").unlink()
        with self.assertRaisesRegex(ValueError, "No stable"):
            update(self.root)
        self.assertEqual(self.text(), README)

    def test_incomplete_markers_do_not_modify_readme(self):
        broken = README + "\n<!-- plugin-badges:start -->\n"
        (self.root / "README.md").write_text(broken, encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Invalid README markers"):
            update(self.root)
        self.assertEqual(self.text(), broken)


if __name__ == "__main__":
    unittest.main()
