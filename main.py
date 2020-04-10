#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import shutil
import functions as fun
from pathlib import Path

(pName, fldLv, delFileTag) = ('Mixtape142ShakeMeDown.m3u', (-2, 2), True)
(IPTH, OPTH) = ('./playlists/', './out/')

# Read the whole m3u file
flines = Path('{}/{}'.format(IPTH, pName)).read_text().splitlines()
# Read head line and count the songs number
(head, flinesNum) = (flines[0], len(flines)-1)
(sInfo, sPath) = (
        [flines[i] for i in range(1, flinesNum, 2)],
        [flines[i] for i in range(2, flinesNum+1, 2)]
    )
# Check m3u file's length for errors
if len(sPath) != len(sInfo):
    sys.exit("There's a problem with the m3u (unequal ids to songs)")
# Main songs loop
with open('{}/{}'.format(OPTH, pName), 'w+') as f:
    f.write('{}\n'.format(head))
    sNum = len(sInfo)
    for i in range(sNum):
        # Start reading playlist pairs
        (info, path) = (fun.clnStr(sInfo[i]), fun.clnStr(sPath[i]))
        (fPath, fName) = (os.path.dirname(path), os.path.basename(path))
        # Amarok prepends a 'file://' tag to the paths
        if delFileTag:
            infPath = path.replace('file://', '')
        else:
            infPath = path
        # Clean and create folder path in output
        outPth = fun.genOutPth(fPath, OPTH, fldLv=fldLv[0])
        Path(outPth).mkdir(parents=True, exist_ok=True)
        oufPath = '{}/{}'.format(outPth, fName)
        # Copy file to the ouput folder
        dest = shutil.copyfile(infPath, oufPath)
        # Writing to the new playlist
        splitPth = oufPath.split(os.path.sep)[fldLv[1]:]
        droidPth = '\\'.join(splitPth)
        f.write('{}\n'.format(droidPth))
