# pyMSync

MTP Playlist Transfer for Amarok-Android music syncing


## Use

### [Copy playlist to folder](./copyPlaylist.py)

Takes an m3u with absolute paths and copies all songs into a new folder (preserving structure), creating a new m3u with relative paths.

### [Change absolute reference](./copyPlaylist.py)

Takes a playlist with an absolute reference and changes it to another given one, whilst saving the new one into the desired folder (useful to convert between iTunes libraries to new ones).

### iTunes Ratings to ID3

Under development.

# Sources

* [M3U](https://en.wikipedia.org/wiki/M3U):
    * [Specification](https://schworak.com/blog/e39/m3u-play-list-specification/)
* Players:
    * [Amarok](https://userbase.kde.org/Amarok/Manual)
    * [VLC](https://www.videolan.org/doc/)
* [ID3](https://en.wikipedia.org/wiki/ID3):
    * [eyeD3](https://eyed3.readthedocs.io/en/latest/eyed3.id3.html#eyed3.id3.frames.PopularityFrame.rating)
    * [Popularimeter](http://id3.org/id3v2.3.0#sec4.18)
* Other tasks
    * [Case-sensitivity handling](https://stackoverflow.com/questions/25843269/can-you-force-os-path-isfile-to-use-case-insensitivity-when-checking-a-file-on)
    * [Verbose option](https://stackoverflow.com/questions/5980042/how-to-implement-the-verbose-or-v-option-into-a-script)
    * [iTunes Rating](https://community.mp3tag.de/t/saving-itunes-rating-and-counter/3803/5)

# Author

Héctor M. Sánchez C.
