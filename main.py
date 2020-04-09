#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import functions as fun
from pathlib import Path

(pName, fldLv, delFileTag) = ('CourteenersLive.m3u', -2, True)
(IPTH, OPTH) = ('./playlists/', './out/')


with open('{}/{}'.format(IPTH, pName)) as f:
    # Read head line
    head = f.readline()
    # Start reading playlist pairs
    (info, path) = (fun.clnStr(f.readline()), fun.clnStr(f.readline()))
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

oufPath
