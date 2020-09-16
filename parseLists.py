
import subprocess
from glob import glob

(playlists, out) = (
        sorted(glob('/mnt/Luma/Music/MX*.m3u'))[:],
        '/mnt/Luma/DroidSync'
    )
# Comand string
fmt = 'python pyMSync.py {} {} -v -o'

for plst in playlists:
    cmnd = fmt.format(plst, out)
    openSP = subprocess.Popen(
            cmnd.split(" ")
        )
    output, err = openSP.communicate()
    # print(output)
