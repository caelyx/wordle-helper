#!/usr/bin/env python3
"""Wordle solver -- works out possible words from a given set of letters."""

import argparse
import os
import re

parser = argparse.ArgumentParser(description="Wordle solver")
parser.add_argument("green", metavar="green", type=str, help="The known pattern, in regex format.")
parser.add_argument(
    "yellow", metavar="yellow", type=str, nargs="?", help="Correct letters in the wrong places."
)
parser.add_argument(
    "grey", metavar="grey", type=str, nargs="?", help="Letters which are not in the solution."
)
args = parser.parse_args()

green = re.compile(args.green)

dir_path = os.path.abspath(os.path.dirname(__file__))
with open(dir_path + "/wordlist.txt", "r") as f:
    wordlist = [line.strip() for line in f if green.match(line.strip())]

for val in wordlist:
    valid = True
    if args.yellow is not None and args.yellow != "-":
        for c in args.yellow:
            if not c in val:
                valid = False
    if args.grey is not None:
        for c in args.grey:
            if c in val:
                valid = False
    if valid:
        print(val)
