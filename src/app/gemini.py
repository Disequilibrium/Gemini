#!/usr/bin/env python3
# Author: Disequilibrium
# Description: This file serves as the program initializer.
#              It may be used to set up the working environment as well.

## BASE LIBRARIES ##
import os
import sys

## GUI LIBRARIES ##
import gui

def run():

    # (I) If these directories don't exist, create them.

    dirs_to_check = [
        "../../configs",
        "../../backups"
    ]

    for dir in dirs_to_check:
        if not os.path.isdir(dir):
            os.mkdir(dir)

    # (II) Launch GUI.

    gui.start()


if __name__ == "__main__":
    run()
