#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import argparse
import functions as fun

# #############################################################################
# This script copies the files from an m3u playlist into a desired folder,
#   along with a new m3u with relative path to the destination. It takes
#   the playlist path, output folder (destination), and the base of the
#   original library (absolute reference to be deleted from the path
#   to make it a relative one).
# #############################################################################

# #############################################################################
# Setup the command line parsing
# #############################################################################
cmdPar = argparse.ArgumentParser(
        prog='pyMSync',
        description='Copies referenced files from an m3u to a destiny folder.',
        epilog='http://chipdelmal.github.io/blog/'
    )
# Positional arguments --------------------------------------------------------
cmdPar.add_argument('iPlst', type=str, help='Input playlist.')
cmdPar.add_argument('oFldr', type=str, help='Output folder.')
# Optional arguments ----------------------------------------------------------
cmdPar.add_argument(
        '-lRt', '--libraryRoot', action='store',
        help='Music library root (for absolute reference removal).'
    )
cmdPar.add_argument(
        '-o', '--overwrite', action='store_true',
        help='Overwrites audio files if they are found in destiny location.'
    )
cmdPar.add_argument(
        '-l', '--log', action='store_true',
        help='Creates a log at the destiny location with a summary of the run.'
    )
cmdPar.add_argument(
        '-v', '--verbose', action='store_true',
        help='Prints the whole process to the terminal.'
    )
# Parse arguments -------------------------------------------------------------
args = cmdPar.parse_args()

# #############################################################################
# Copy the playlist
# -----------------------------------------------------------------------------
# PLST: Input playlist file (absolute m3u)
# OPTH: Base output path
# LPTH: Base music library path (original path to be removed from the plst)
# #############################################################################
(PLST, OPTH, LPTH) = (args.iPlst, args.oFldr, args.libraryRoot)
# Original playlist is stored at the library root
if args.libraryRoot is None:
    LPTH = os.path.split(PLST)[0]
fun.copyPlaylistToDir(
        PLST, OPTH, LPTH,
        overwrite=args.overwrite, log=args.log, verbose=args.verbose
    )
