# pyMSync

These scripts were created for people like me, who still have a large amount of their music collection in files and need to sync them across devices.

The original target application was to export an absolute-referenced [M3U](https://en.wikipedia.org/wiki/M3U) from either [iTunes](https://www.apple.com/itunes/) or [Amarok](https://amarok.kde.org/) to an [Android](https://www.android.com/) phone (mainly because I got tired of depending of third-party applications to do the music syncs between my computer and my phone). These scripts, however, can be used to copy playlists to arbitrary folders to make the sharing of music and playlists easier.

<hr>

## Use

The scripts take extended playlists formatted as follows:

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
Where each pair of lines holds the information/path to a song. It automatically removes the `file://` prepend, and handles case-sensitive paths for Linux.

Not extended playlists are to be formatted as follows (with or without the `file://` tag):

```
file:///media/hdd/Music/Courteeners/ANNA/01 Are You in Love With a Notion_.mp3
file:///media/hdd/Music/Coldplay/A Rush of Blood to the Head/04 The Scientist.mp3
file:///media/hdd/Music/Cage The Elephant/Thank You, Happy Birthday/2-04 Shake Me Down (acoustic).mp3
file:///media/hdd/Music/EELS/Shootenanny!/05 Dirty Girl.mp3
file:///media/hdd/Music/Courteeners/Falcon/1-01 The Opener.mp3
file:///media/hdd/Music/Coldplay/A Rush of Blood to the Head/04 The Scientist.mp3
file:///media/hdd/Music/Blind Pilot/And Then Like Lions/01 Umpqua Rushing.mp3
file:///media/hdd/Music/Coldplay/Viva la Vida or Death and All His Friends/1-07 Viva la Vida.mp3
file:///media/hdd/Music/EELS/Beautiful Freak/06 My Beloved Monster.mp3
file:///media/hdd/Music/Cigarettes After Sex/Cigarettes After Sex/04 Apocalypse.m4a
file:///media/hdd/Music/Coldplay/Viva la Vida or Death and All His Friends/1-07 Viva la Vida.mp3
file:///media/hdd/Music/Hozier/Hozier (Deluxe Version)/1-04 Someone New.mp3
file:///media/hdd/Music/Cage The Elephant/Unpeeled/02 Whole Wide World.mp3
file:///media/hdd/Music/Yuck/Glow & Behold/11 Glow & Behold.mp3
```

Example of use:

This run will take the 'Mixtape127_TonightTonight.m3u' playlist, and copies the referenced audio files to the '/Sync/Mixtapes' folder with a new m3u placed at its root.

```bash
python pyMSync.py \
    '/media/hdd/Music/Mixtape127_TonightTonight.m3u' \
    '/home/chipdelmal/Sync/Mixtapes' \
    -o -l -v
```

The description of the arguments being:

```
positional arguments:
iPlst: Input playlist absolute path.
oFldr: Output folder absolute path.      

optional arguments:
-o   [--overwrite]: Overwrites audio files if they are found in destiny location.
-l   [--log]: Creates a log at the destiny location with a summary of the run.
-v   [--verbose]: Prints the whole process to the terminal.
-lRt [--libraryRoot]: Music library root (for absolute reference removal). Leave blank if the m3u is stored at the library root.
```

### [Transfer playlist](./pyMSync.py)

Takes an M3U file from the system, copies the songs that are referenced in the playlist into a selected destination (preserving the folder structure), and creates an equivalent M3U relative-path file at the root of the selected folder.

### [Change absolute reference](./chgAbsRef.py)

Takes a playlist with an absolute reference and changes it to another given one, whilst saving the new one into the desired folder (useful to transfer libraries across devices).

## Dependencies

* [unidecode](https://pypi.org/project/Unidecode/)

<hr>

## To-Do

* Relative-referenced M3U.
* Test in Windows filesystems (only UNIX has been tested).

<hr>

# Sources

* [M3U](https://en.wikipedia.org/wiki/M3U): [Specification](https://schworak.com/blog/e39/m3u-play-list-specification/)
* Players: [Amarok](https://userbase.kde.org/Amarok/Manual), [VLC](https://www.videolan.org/doc/)
* [ID3](https://en.wikipedia.org/wiki/ID3): [eyeD3](https://eyed3.readthedocs.io/en/latest/eyed3.id3.html#eyed3.id3.frames.PopularityFrame.rating), [Popularimeter](http://id3.org/id3v2.3.0#sec4.18)
* Other tasks: [Case-sensitivity handling](https://stackoverflow.com/questions/25843269/can-you-force-os-path-isfile-to-use-case-insensitivity-when-checking-a-file-on), [verbose option](https://stackoverflow.com/questions/5980042/how-to-implement-the-verbose-or-v-option-into-a-script), [iTunes r¡ating](https://community.mp3tag.de/t/saving-itunes-rating-and-counter/3803/5)

<hr>

# Author

<img src="./media/pusheen.jpg" height="130px" align="middle"><br>

[Héctor M. Sánchez C.](https://chipdelmal.github.io/)
