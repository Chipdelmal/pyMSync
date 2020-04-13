
import os
import sys
import shutil
from pathlib import Path


def clnStr(inString):
    tmpStr = inString.strip().replace('%20', ' ')
    return tmpStr


def genOutPth(fPath, OPTH, LPTH):
    tmpFull = OPTH + fPath.replace(LPTH, '')
    return os.path.dirname(tmpFull)


def chkPlstLen(sPath, sInfo):
    if len(sPath) != len(sInfo):
        sys.exit("There's a problem with the m3u (unequal ids to songs)")
    return True


def rmvFileTag(path, delFileTag=True):
    if delFileTag:
        infPath = path.replace('file://', '')
    else:
        infPath = path
    return infPath


def parsePlaylist(IPTH):
    # Read the whole m3u file
    flines = Path(IPTH).read_text().splitlines()
    # Read head line and count the songs number
    (head, flinesNum) = (flines[0], len(flines)-1)
    (sInfo, sPath) = (
            [flines[i] for i in range(1, flinesNum, 2)],
            [flines[i] for i in range(2, flinesNum+1, 2)]
        )
    return (head, flinesNum, sInfo, sPath)


def writePlistLine(f, oufPath, OPTH):
    droidPth = './' + oufPath.replace(OPTH, '')
    f.write('{}\n'.format(droidPth))
    return True


def copyPlaylistToDir(playlist, outputPath, libraryPath, delFileTag=True):
    # Read the whole m3u file
    (head, flinesNum, sInfo, sPath) = parsePlaylist(playlist)
    # Check m3u file's length for errors
    chkPlstLen(sPath, sInfo)
    pName = os.path.basename(playlist)
    # Main songs loop
    with open('{}/{}'.format(outputPath, pName), 'w+') as f:
        f.write('{}\n'.format(head))
        sNum = len(sInfo)
        for i in range(sNum):
            # Start reading playlist pairs
            (info, path) = (clnStr(sInfo[i]), clnStr(sPath[i]))
            (_, fName) = (os.path.dirname(path), os.path.basename(path))
            # Amarok prepends a 'file://' tag to the paths
            infPath = rmvFileTag(path, delFileTag=delFileTag)
            # Clean and create folder path in output
            outPth = genOutPth(infPath, outputPath, libraryPath)
            Path(outPth).mkdir(parents=True, exist_ok=True)
            print(outPth)
            oufPath = '{}/{}'.format(outPth, fName)
            # Copy file to the ouput folder
            shutil.copyfile(infPath, oufPath)
            # Writing to the new playlist
            f.write(info+'\n')
            writePlistLine(f, oufPath, outputPath)
