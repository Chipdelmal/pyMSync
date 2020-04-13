#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
import functions as fun

iPth = '/home/chipdelmal/Documents/Github/pyDroid/playlist/iTunes/'
oPth = '/media/hdd/Music/'
bOld = '/Users/glados/Music/Music/Media.localized/'
bNew = '/media/hdd/Music/'

allPlsts = glob.glob(iPth + '*.m3u')
for plst in allPlsts:
    fun.fixPlistReference(plst, oPth, bOld, bNew, ClnPath=True)
