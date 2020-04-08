
import os


def clnStr(inString):
    tmpStr = inString.strip().replace('%20', ' ')
    return tmpStr


def genOutPth(fPath, OPTH, fldLv=-2):
    pthSplit = fPath.split(os.path.sep)[fldLv:]
    pthJoin = os.path.join(OPTH, *pthSplit)
    return pthJoin
