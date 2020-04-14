#!/usr/bin/python
# -*- coding: utf-8 -*-

import glob
import functions as fun


# #############################################################################
# This script copies the files from an m3u playlist into a desired folder,
#   along with a new m3u with relative path to the destination.
# -----------------------------------------------------------------------------
# iPth: Input path where the m3u file(s) is/are located
# oPth: Output path for the new m3u file
# bOld: Base music library path
# bNew:
# #############################################################################
iPth = '/home/chipdelmal/Documents/Github/pyDroid/playlist/iTunes/'
oPth = '/media/hdd/Music/'
bOld = '/Users/glados/Music/Music/Media.localized/'
bNew = '/media/hdd/Music/'


# #############################################################################
# Single
# #############################################################################
pName = 'Mixtape001_ NewIndie.m3u'
fun.fixPlistReference(iPth + pName, oPth, bOld, bNew, ClnPath=True)

# #############################################################################
# Batch
# #############################################################################
allPlsts = glob.glob(iPth + '*.m3u')
for plst in allPlsts:
    fun.fixPlistReference(plst, oPth, bOld, bNew, ClnPath=True)
