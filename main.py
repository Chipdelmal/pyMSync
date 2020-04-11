#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import functions as fun
from pathlib import Path

(pName, fldLv, delFileTag) = ('Mixtape142ShakeMeDown.m3u',(6, 2), True)
(DT, EXT) = (True, True)
(IPTH, OPTH) = ('./playlists/', './out/')
# (IPTH, OPTH) = (
#          './playlists/',
#          '/run/user/1000/gvfs/mtp:host=%5Busb%3A003%2C013%5D/Samsung SD card/Music/'
#      )
# Read the whole m3u file
(head, flinesNum, sInfo, sPath) = fun.parsePlaylist(IPTH, pName)
# Check m3u file's length for errors
fun.chkPlstLen(sPath, sInfo)
# Main songs loop
with open('{}/{}'.format(OPTH, pName), 'w+') as f:
    f.write('{}\n'.format(head))
    sNum = len(sInfo)
    for i in range(sNum):
        # Start reading playlist pairs
        (info, path) = (fun.clnStr(sInfo[i]), fun.clnStr(sPath[i]))
        (fPath, fName) = (os.path.dirname(path), os.path.basename(path))
        # Amarok prepends a 'file://' tag to the paths
        infPath = fun.rmvFileTag(path, delFileTag=delFileTag)
        # Clean and create folder path in output
        outPth = fun.genOutPth(fPath, OPTH, fldLv=fldLv[0])
        Path(outPth).mkdir(parents=True, exist_ok=True)
        oufPath = '{}/{}'.format(outPth, fName)
        # Copy file to the ouput folder
        dest = shutil.copyfile(infPath, oufPath)
        # Writing to the new playlist
        if EXT:
            f.write(info+'\n')
        if DT:
            fun.writeDTPlistLine(oufPath, f, fldLv)
        else:
            fun.writePlistLine(oufPath, f, fldLv)
