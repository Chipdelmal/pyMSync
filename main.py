#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import functions as fun
from pathlib import Path

(pName, fldLv) = ('CourteenersLive.m3u', -2)
(IPTH, OPTH) = ('./playlists/', './out/')


with open('{}/{}'.format(IPTH, pName)) as f:
    # Read head line
    head = f.readline()
    # Start reading playlist pairs
    (info, path) = (fun.clnStr(f.readline()), fun.clnStr(f.readline()))
    (fPath, fName) = (os.path.dirname(path), os.path.basename(path))
    # Clean and create folder path in output
    outPth = fun.genOutPth(fPath, OPTH, fldLv=-2)
    Path(outPth).mkdir(parents=True, exist_ok=True)
