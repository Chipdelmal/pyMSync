
import subprocess
from glob import glob

(playlists, out) = (
        sorted(glob('/media/hdd/Music/SM*.m3u'))[:],
        '/media/chipdelmal/cache/DroidSync'
    )
# Comand string
fmt = 'python pyMSync.py {} {} -v -o'

fmt.format(, '/media/chipdelmal/cache/DroidSync')

for plst in playlists:
    cmnd = fmt.format(plst, out)
    openSP = subprocess.Popen(
            cmnd.split(" ")
        )
    output, err = openSP.communicate()
    # print(output)
