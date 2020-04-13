#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import functions as fun


iPth = '/home/chipdelmal/Documents/Github/pyDroid/playlist/iTunes/Mixtape001_ NewIndie.m3u'
oPth = '/home/chipdelmal/Documents/Github/pyDroid/playlist/Amarok/'
bOld = '/Users/glados/Music/Music/Media.localized/'
bNew = '/media/hdd/Music/'
ClnPath = True

# Read playlist
(head, flinesNum, sInfo, sPath) = fun.parsePlaylist(iPth)
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
        (info, path) = (fun.clnStr(sInfo[i]), fun.clnStr(cPth[i]))
        f.write(info+'\n')
        f.write(path+'\n')
