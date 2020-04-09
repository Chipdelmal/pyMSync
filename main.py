#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import shutil
import functions as fun
from pathlib import Path

(pName, fldLv, delFileTag) = ('CourteenersLive.m3u', -2, True)
(IPTH, OPTH) = ('./playlists/', './out/')


flines = Path('{}/{}'.format(IPTH, pName)).read_text().splitlines()

# Read head line and count the songs number
(head, flinesNum) = (flines[0], len(flines) - 1)
(sInfo, sPath) = (
        [flines[i] for i in range(1, flinesNum, 2)],
        [flines[i] for i in range(2, flinesNum+1, 2)]
    )
if len(sPath) != len(sInfo):
    sys.exit("There's a problem with the m3u (unequal ids to songs)")

sNum = len(sInfo)
for i in range(sNum):
    # Start reading playlist pairs
    (info, path) = (fun.clnStr(sInfo[i]), fun.clnStr(sPath[i]))
    (fPath, fName) = (os.path.dirname(path), os.path.basename(path))
    if delFileTag:
        infPath = path.replace('file://', '')
    else:
        infPath = path
    # Clean and create folder path in output
    outPth = fun.genOutPth(fPath, OPTH, fldLv=-2)
    Path(outPth).mkdir(parents=True, exist_ok=True)
    oufPath = '{}/{}'.format(outPth, fName)
    # Copy file to the ouput folder
    dest = shutil.copyfile(infPath, oufPath)
