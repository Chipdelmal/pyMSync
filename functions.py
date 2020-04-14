
import os
import sys
import shutil
from pathlib import Path


def clnStr(inString):
    # Changes the %20 ASCII to space.
    tmpStr = inString.strip().replace('%20', ' ')
    return tmpStr


def genOutPth(fPath, OPTH, LPTH):
    # Switch core of paths so that a new folder structure can be generated
    #   in the new location (LPTH to OPTH in fPath).
    tmpFull = OPTH + fPath.replace(LPTH, '')
    return os.path.dirname(tmpFull)


def chkPlstLen(sPath, sInfo):
    # Checks if the paths and info lists are the same length and exits if they
    #   are not.
    if len(sPath) != len(sInfo):
        sys.exit("There's a problem with the m3u (unequal ids to songs)")
    return True


def rmvFileTag(path, delFileTag=True):
    # Deletes the 'file://' tag that iTunes and Amarok add to absolute paths.
    if delFileTag:
        infPath = path.replace('file://', '')
    else:
        infPath = path
    return infPath


def parsePlaylist(IPTH):
    # Reads an extended m3u file, splits the info and paths info into lists,
    #   and returns the head, lines number, song info, and song paths.
    flines = Path(IPTH).read_text().splitlines()
    # Read head line and count the songs number
    (head, flinesNum) = (flines[0], len(flines)-1)
    (sInfo, sPath) = (
            [flines[i] for i in range(1, flinesNum, 2)],
            [flines[i] for i in range(2, flinesNum+1, 2)]
        )
    return (head, flinesNum, sInfo, sPath)


def writePlistLine(f, oufPath, OPTH):
    # Replaces an absolute path with a relative one and writes a line to the
    #   m3u file connection 'f'.
    droidPth = './' + oufPath.replace(OPTH, '')
    f.write('{}\n'.format(droidPth))
    return True


def copyPlaylistToDir(playlist, outputPath, libraryPath, delFileTag=True):
    # Copies a playlist to an output path and generates a new, relative, M3U
    #   at the base of the new library path. Currently needs an extended,
    #   absolute path, M3U.
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


def fixPlistReference(iPth, oPth, bOld, bNew, ClnPath=False):
    # Changes the paths between two absolute-referenced libraries paths
    #   in a M3U extended playlist.
    (head, flinesNum, sInfo, sPath) = parsePlaylist(iPth)
    # Clean paths and names
    cPth = [sp.replace(bOld, bNew) for sp in sPath]
    nPls = os.path.basename(iPth)
    if ClnPath:
        oFil = oPth + nPls.replace(' ', '')
    else:
        oFil = oPth + nPls
    # Write to file
    with open(oFil, 'w+') as f:
        f.write('{}\n'.format(head))
        sNum = len(sInfo)
        for i in range(sNum):
            (info, path) = (clnStr(sInfo[i]), clnStr(cPth[i]))
            f.write(info+'\n')
            f.write(path+'\n')
