# pyMSync

These scripts were created for people like me, who still have a large amount of their music collection in files and need to sync them across devices.

The original target application was to export an absolute-referenced [M3U](https://en.wikipedia.org/wiki/M3U) from either [iTunes](https://www.apple.com/itunes/) or [Amarok](https://amarok.kde.org/) to an [Android](https://www.android.com/) phone (mainly because I got tired of depending of third-party applications to do the music syncs between my computer and my phone). These scripts, however, can be used to copy playlists to arbitrary folders to make the sharing of music and playlists easier.

<hr>

## Use

The scripts take playlists formatted as follows:

```
#EXTM3U
#EXTINF:237,Like A Friend - Pulp
/media/hdd/Music/Pulp/Great Expectations/14 Like A Friend.mp3
#EXTINF:254,Umpqua Rushing - Blind Pilot
/media/hdd/Music/Blind Pilot/And Then Like Lions/01 Umpqua Rushing.mp3
#EXTINF:163,Wake Me - Bleachers
/media/hdd/Music/Bleachers/Strange Desire/05 Wake Me.mp3
#EXTINF:199,A Little Respect - Wheatus
/media/hdd/Music/Wheatus/Wheatus/04 A Little Respect.mp3
#EXTINF:151,Surfing In The Sky - The Vaccines
/media/hdd/Music/The Vaccines/Combat Sports/04 Surfing In The Sky.mp3
#EXTINF:290,Apocalypse - Cigarettes After Sex
/media/hdd/Music/Cigarettes After Sex/Cigarettes After Sex/04 Apocalypse.m4a
#EXTINF:235,Sugartown - The Fratellis
/media/hdd/Music/The Fratellis/In Your Own Sweet Time/03 Sugartown.mp3
#EXTINF:267,3 Rounds and a Sound - Blind Pilot
/media/hdd/Music/Blind Pilot/3 Rounds and a Sound/11 3 Rounds and a Sound.mp3
#EXTINF:284,Honey and the Moon - Joseph Arthur
/media/hdd/Music/Joseph Arthur/Redemption's Son/1-02 Honey and the Moon.mp3
#EXTINF:233,(All Afternoon) In Love - The Vaccines
/media/hdd/Music/The Vaccines/English Graffiti/05 (All Afternoon) In Love.mp3
```

Where each pair of lines holds the information/path to a song. It can the `file://` prepend, and handles case-sensitive paths for linux.

### [Transfer playlist](./copyPlaylist.py)

Takes an M3U file from the system, copies the songs that are referenced in the playlist into a selected destination (preserving the folder structure), and creates an equivalent M3U relative-path file at the root of the selected folder.

### [Change absolute reference](./chgAbsRef.py)

Takes a playlist with an absolute reference and changes it to another given one, whilst saving the new one into the desired folder (useful to transfer libraries across devices).

<hr>

## To-Do

* Non-extended playlist support (without `#EXTINF` lines).
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
