<div align="center">

# Nari Extras

**Small upgrades for your everyday listening.**

Community plugins for [Nari](https://narimusic.com): listening stats, a cleaner queue, and your music sources one tap away.

<!-- plugin-badges:start -->
[![Listening Wrapped 1.3.2](https://img.shields.io/badge/Listening_Wrapped-1.3.2-ed4963?style=for-the-badge)](https://github.com/Pirate2122yt/Nari-Extras/tree/main/Plugins/Listening-Wrapped)
[![Queue Tools 1.0.3](https://img.shields.io/badge/Queue_Tools-1.0.3-4cba7b?style=for-the-badge)](https://github.com/Pirate2122yt/Nari-Extras/tree/main/Plugins/Queue-Tools)
[![Source Switcher 1.2.3](https://img.shields.io/badge/Source_Switcher-1.2.3-009ff3?style=for-the-badge)](https://github.com/Pirate2122yt/Nari-Extras/tree/main/Plugins/Source-Switcher)
<!-- plugin-badges:end -->

**By [Pirate2122yt](https://github.com/Pirate2122yt)**

[Browse the repository](https://github.com/Pirate2122yt/Nari-Extras) · [Install](#installation) · [Update](#updates) · [Report an issue](https://github.com/Pirate2122yt/Nari-Extras/issues)

</div>

---

## The plugins

<!-- plugin-downloads:start -->
| Plugin | What it does | Download |
| :--- | :--- | :---: |
| 🔴 **[Listening Wrapped](https://github.com/Pirate2122yt/Nari-Extras/tree/main/Plugins/Listening-Wrapped)** | Your month or year in music, with top songs, artists, albums, and listening time. | [**v1.3.2 · ZIP**](https://github.com/Pirate2122yt/Nari-Extras/raw/refs/heads/main/Plugins/Listening-Wrapped/listening-wrapped-1.3.2.zip) |
| 🟢 **[Queue Tools](https://github.com/Pirate2122yt/Nari-Extras/tree/main/Plugins/Queue-Tools)** | Remove duplicates, shuffle upcoming songs, and choose how many songs each artist gets. | [**v1.0.3 · ZIP**](https://github.com/Pirate2122yt/Nari-Extras/raw/refs/heads/main/Plugins/Queue-Tools/queue-tools-1.0.3.zip) |
| 🔵 **[Quick Source Switcher](https://github.com/Pirate2122yt/Nari-Extras/tree/main/Plugins/Source-Switcher)** | Choose your music sources and switch between them with a corner button. | [**v1.2.3 · ZIP**](https://github.com/Pirate2122yt/Nari-Extras/raw/refs/heads/main/Plugins/Source-Switcher/source-switcher-1.2.3.zip) |
<!-- plugin-downloads:end -->
The download links above point directly to the installable ZIPs. Each linked plugin folder also contains its available versions.

### Listening Wrapped

Give your listening history a home.

- Browse monthly and yearly reports with top songs, artists, and albums.
- See approximate listening minutes, active days, streaks, and new discoveries.
- Save a summary card or export a history backup.
- Keep long-term history locally, with no fixed record cap.

**Open:** Home → Listening Wrapped, or Now Playing → Wrapped.

Tracking starts when the plugin is enabled. Earlier listening cannot be recreated. Available storage and Nari's memory budget still apply.

### Queue Tools

Make the next few songs a better fit.

- Remove upcoming copies of the same song.
- Shuffle upcoming songs while keeping your current track and playback position.
- Keep up to **1, 2, 3, 5, or 10 songs per artist**.
- Use the tools with queues started from playlists, albums, liked songs, or your library.

**Open:** Home → Queue Tools, or Now Playing → Queue tools.

Playlist menus also include **Play with Queue Tools…**. That option starts a fresh queue from the selected playlist. Your saved playlist stays unchanged.

### Quick Source Switcher

Move between your music libraries with a tap.

- Pick two or more available sources and choose their switching order.
- Switch using the red corner button.
- Right-click or long-press the button to change your choices.
- Keep unavailable sources saved; they are skipped until enabled again.

**Open:** The corner button, Now Playing → Sources, or the plugin's settings.

Switching stops playback and opens your tracks. Sources must already be installed and configured in Nari. Services such as Navidrome, Spotify, or YouTube Music appear only when a compatible provider is available and enabled.

## Installation

1. Download a plugin's **ZIP** using the table above. Keep it zipped. If browsing a plugin folder on GitHub, open the ZIP and choose **Download raw file**.
2. In Nari, open **Settings → Plugins → Install plugin**.
3. Choose the downloaded ZIP, then enable the plugin.
4. Open it using the location listed above.

You can install any combination of them.

## Updates

Check the [plugin folders](https://github.com/Pirate2122yt/Nari-Extras/tree/main/Plugins) for updates, then install the newer ZIP over the existing plugin. Keeping the same plugin ID lets Nari retain its saved settings and Wrapped history.

Reload the plugin or restart Nari if the previous icon or interface is still showing. Export a Wrapped history backup before uninstalling it: uninstalling removes its local data.

## Make them yours

To customize a plugin, extract its ZIP. Inside are an editable `manifest.json` for its name, description, and author, plus vector artwork:

| File | Used for |
| :--- | :--- |
| `icon.svg` | The white symbol used inside Nari's controls |
| `logo.svg` | The editable colored logo |
| `logo.png` | The logo shown in the plugin list |

Keep `id`, `api`, and `main` unchanged when customizing a plugin. After editing, zip the plugin's files with `manifest.json` at the archive root.

## Feedback

Found a bug or have an idea? [Open an issue in Nari Extras](https://github.com/Pirate2122yt/Nari-Extras/issues/new). Include the plugin name and version, your Nari version, your device or operating system, and the steps to reproduce the problem. Screenshots help with layout issues.

---

<div align="center">

**Made by Pirate2122yt for [Nari](https://narimusic.com).**

Nari is created by [NaviVani](https://github.com/NaviVani-dev/Nari). These plugins are community projects.

</div>
