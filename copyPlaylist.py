#!/usr/bin/python
# -*- coding: utf-8 -*-

from pathlib import Path
import functions as fun

# #############################################################################
# This script copies the files from an m3u playlist into a desired folder,
#   along with a new m3u with relative path to the destination.
# -----------------------------------------------------------------------------
# PLST: Input playlist file (absolute m3u)
# OPTH: Base output path
# LPTH: Base music library path
# #############################################################################
pName = '4&5.m3u'
(PLST, OPTH, LPTH) = (
        '/home/chipdelmal/Documents/Github/pyDroid/playlist/Amarok/'+pName,
        '/home/chipdelmal/Dropbox/Mixtapes/',
        '/media/hdd/Music/'
    )
fun.copyPlaylistToDir(PLST, OPTH, LPTH, overwrite=True)
