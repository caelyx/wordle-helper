#!/usr/bin/env python3
"""Wordle solver -- works out possible words from a given set of letters."""

import argparse
import os
import re


def search(args):
    green = re.compile(args.green)

    # Locate the directory containing this file and the word list
    dir_path = os.path.abspath(os.path.dirname(__file__))

    # Open the word list and filter for words matching the green pattern
    with open(dir_path + "/wordlist.txt", "r", encoding="ascii") as f:
        wordlist = [line.strip() for line in f if green.match(line.strip())]

    results = []

    for thisWord in wordlist:
        valid = True

        # Check each of the yellow letters is in the word
        if args.yellow is not None and args.yellow != "-":
            for c in args.yellow:
                if not c in thisWord:
                    valid = False

        # Check that none of the grey letters is in the word
        if args.grey is not None:
            for c in args.grey:
                if c in thisWord:
                    valid = False

        if valid:
            results.append(thisWord)
    return results


def main():
    parser = argparse.ArgumentParser(description="Wordle solver")

    parser.add_argument(
        "green", metavar="green", type=str, help="The known pattern, in regex format."
    )
    parser.add_argument(
        "grey", metavar="grey", type=str, nargs="?", help="Letters which are not in the solution."
    )
    parser.add_argument(
        "yellow", metavar="yellow", type=str, nargs="?", help="Correct letters in the wrong places."
    )
    args = parser.parse_args()

    for valid_word in search(args):
        print(valid_word)


if __name__ == "__main__":
    main()
