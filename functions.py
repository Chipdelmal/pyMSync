
import os
import sys
from pathlib import Path


def clnStr(inString):
    tmpStr = inString.strip().replace('%20', ' ')
    return tmpStr


def genOutPth(fPath, OPTH, fldLv=-2):
    pthSplit = fPath.split(os.path.sep)[fldLv:]
    pthJoin = os.path.join(OPTH, *pthSplit)
    return pthJoin


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


def parsePlaylist(IPTH, pName):
    # Read the whole m3u file
    flines = Path('{}/{}'.format(IPTH, pName)).read_text().splitlines()
    # Read head line and count the songs number
    (head, flinesNum) = (flines[0], len(flines)-1)
    (sInfo, sPath) = (
            [flines[i] for i in range(1, flinesNum, 2)],
            [flines[i] for i in range(2, flinesNum+1, 2)]
        )
    return (head, flinesNum, sInfo, sPath)


def writeDTPlistLine(oufPath, f, fldLv):
    splitPth = oufPath.split(os.path.sep)[fldLv[1]:]
    droidPth = '\\'.join(splitPth)
    f.write('{}\n'.format(droidPth))
    return True


def writePlistLine(oufPath, f, fldLv):
    splitPth = oufPath.split(os.path.sep)[fldLv[1]:]
    droidPth = './' + '/'.join(splitPth)
    f.write('{}\n'.format(droidPth))
    return True
