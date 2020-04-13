#!/usr/bin/python
# -*- coding: utf-8 -*-

import functions as fun

# #############################################################################
# This script copies the files from an m3u playlist into a desired folder,
#   along with a new m3u with relative path to the destination.
# -----------------------------------------------------------------------------
# PLST: Input playlist file (absolute m3u)
# OPTH: Base output path
# LPTH: Base music library path
# #############################################################################
pName = 'Mixtape142ShakeMeDown.m3u'
(PLST, OPTH, LPTH) = (
        '/home/chipdelmal/Documents/Github/pyDroid/plst/Amarok/'+pName,
        '/home/chipdelmal/Dropbox/Mixtapes/',
        '/media/hdd/Music/'
    )
fun.copyPlaylistToDir(PLST, OPTH, LPTH)
