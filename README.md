# pyMSync

These scripts were created for people like me, who still have a large amount of their music collection in files and need to sync them across devices.

The original target application was to export an absolute-referenced [M3U](https://en.wikipedia.org/wiki/M3U) from either [iTunes](https://www.apple.com/itunes/) or [Amarok](https://amarok.kde.org/) to an [Android](https://www.android.com/) phone (mainly because I got tired of depending of third-party applications to do the music syncs between my computer and my phone). These scripts, however, can be used to copy playlists to arbitrary folders to make the sharing of music and playlists easier.

<hr>

## Use

### [Transfer playlist](./copyPlaylist.py)

Takes an M3U file from the system, copies the songs that are referenced in the playlist into a selected destination (preserving the folder structure), and creates an equivalent M3U relative-path file at the root of the selected folder.

### [Change absolute reference](./chgAbsRef.py)

Takes a playlist with an absolute reference and changes it to another given one, whilst saving the new one into the desired folder (useful to transfer libraries across devices).

<hr>

## To-Do

* Relative-referenced M3U.
* Test in Windows filesystems (only UNIX has been tested).

<hr>

# Sources

* [M3U](https://en.wikipedia.org/wiki/M3U): [Specification](https://schworak.com/blog/e39/m3u-play-list-specification/)
* Players: [Amarok](https://userbase.kde.org/Amarok/Manual), [VLC](https://www.videolan.org/doc/)
* [ID3](https://en.wikipedia.org/wiki/ID3): [eyeD3](https://eyed3.readthedocs.io/en/latest/eyed3.id3.html#eyed3.id3.frames.PopularityFrame.rating), [Popularimeter](http://id3.org/id3v2.3.0#sec4.18)
* Other tasks: [Case-sensitivity handling](https://stackoverflow.com/questions/25843269/can-you-force-os-path-isfile-to-use-case-insensitivity-when-checking-a-file-on), [Verbose option](https://stackoverflow.com/questions/5980042/how-to-implement-the-verbose-or-v-option-into-a-script), [iTunes Rating](https://community.mp3tag.de/t/saving-itunes-rating-and-counter/3803/5)

<hr>

# Author

<img src="./media/pusheen.jpg" height="130px" align="middle"><br>

[Héctor M. Sánchez C.](https://chipdelmal.github.io/)
