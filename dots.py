#!/usr/bin/env python3

import os
import sys
import argparse

# Specify dir where all themes are located
# It should have the following structure
# └── themes
#    ├── dracula
#    └── gruvbox
theme_dir = "/home/talhah/themes/"
theme = ""

parser = argparse.ArgumentParser()
parser.add_argument("-d","--dir",help="Path to directory containing themes")
parser.add_argument("-t","--theme",help="Name of theme")
args = parser.parse_args()

if args.dir != None:
    theme_dir = args.dir

if args.theme != None:
    theme = args.theme

if not os.path.exists(os.path.join(theme_dir,theme)):
    print("Given theme does not exist, please try again")
    sys.exit(1)
else:
    os.chdir(theme_dir)
    if theme == "":
        themes = os.listdir()
        if len(themes) == 0:
            print("No themes were found in given directory, please try again")
            sys.exit(1)
        else:
            # Give user choice to choose themes
            input_message = "Pick a theme:\n"
            for index, item in enumerate(themes):
                input_message += f'{index+1}) {item}\n'
            input_message += "Your choice: "
            theme = ""
            while theme not in map(str, range(1, len(themes) + 1)):
                theme = input(input_message)
    else:
        if not os.path.exists(os.path.join(theme_dir,theme)):
            print("Given theme does not exist, please try again")
            sys.exit(1)
        os.chdir(theme)
