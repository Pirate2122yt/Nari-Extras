# Automatic download links for Nari Extras

Upload these three files to **Pirate2122yt/Nari-Extras**, preserving their paths:

```text
.github/workflows/update-plugin-links.yml
tools/update_readme.py
tools/test_update_readme.py
```

Commit them to `main`. The workflow runs on that first upload, then whenever plugin ZIPs or the README change. You can also run **Actions → Update plugin download links → Run workflow**.

After setup, upload new plugin versions into the existing folders:

```text
Plugins/Listening-Wrapped/listening-wrapped-1.3.2.zip
Plugins/Queue-Tools/queue-tools-1.0.3.zip
Plugins/Source-Switcher/source-switcher-1.2.3.zip
```

Keep the `name-X.Y.Z.zip` naming pattern and make sure `manifest.json` inside each ZIP has the matching version and plugin ID. The updater selects the highest stable version number. Older uploads cannot downgrade a link while a newer ZIP remains in the folder. Prerelease filenames such as `1.4.0-beta.zip` are ignored.

The bot updates the three version badges and the download table, then commits `README.md` automatically. Your introduction, instructions, feedback section, and other text are preserved. No personal access token or Python dependencies are needed.

On the first run, the script recognizes your current README and adds `plugin-badges` and `plugin-downloads` HTML comment markers. Keep these markers. Text inside them is generated; other sections stay editable. To change generated plugin descriptions, edit `PLUGINS` in `tools/update_readme.py`.

If a ZIP is invalid or its manifest does not match its filename, the workflow fails without rewriting the README. Fix the ZIP and upload it again.

If GitHub rejects the bot's commit, check **Settings → Actions → General → Workflow permissions** and allow read/write access. Repository or organization rules that require pull requests can also prevent direct bot commits to `main`.

The workflow only commits `README.md`. It leaves all ZIPs in place and does not publish releases or change plugin data.

See [GitHub's workflow documentation](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow) for event and permission behavior.
