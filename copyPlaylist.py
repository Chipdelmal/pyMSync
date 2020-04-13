#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import functions as fun
from pathlib import Path

###############################################################################
# Desktop (Git)
###############################################################################
(PLST, OPTH, LPTH) = (
        '/home/chipdelmal/Documents/Github/ADroidMusicSync/playlists/Amarok/Cage.m3u',
        '/home/chipdelmal/Dropbox/Mixtapes/',
        '/media/hdd/Music/'
    )

# Read the whole m3u file
(head, flinesNum, sInfo, sPath) = fun.parsePlaylist(PLST, '')
# Check m3u file's length for errors
nErr = fun.chkPlstLen(sPath, sInfo)
pName = os.path.basename(PLST)
# Main songs loop
with open('{}/{}'.format(OPTH, pName), 'w+') as f:
    f.write('{}\n'.format(head))
    sNum = len(sInfo)
    for i in range(sNum):
        # Start reading playlist pairs
        (info, path) = (fun.clnStr(sInfo[i]), fun.clnStr(sPath[i]))
        (fPath, fName) = (os.path.dirname(path), os.path.basename(path))
        # Amarok prepends a 'file://' tag to the paths
        infPath = fun.rmvFileTag(path, delFileTag=True)
        # Clean and create folder path in output
        outPth = fun.genOutPth(infPath, OPTH, LPTH)
        Path(outPth).mkdir(parents=True, exist_ok=True)
        oufPath = '{}/{}'.format(outPth, fName)
        # Copy file to the ouput folder
        dest = shutil.copyfile(infPath, oufPath)
        # Writing to the new playlist
        f.write(info+'\n')
        fun.writePlistLine(f, oufPath, OPTH)
