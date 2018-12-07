#!/usr/bin/env python3
import re

"""
Advent of Code 2018
Puzzle #3 - 2018-12-03: Identifying Claim Overlaps - Part 1
# https://adventofcode.com/2018/day/3
Given a list of claimed territory, find how much area is double-claimed.

Input (via stdin): "#claim_id @ cells_from_leftmost,cells_from_top: widthxheight e.g.:
#1 @ 872,519: 18x18
#2 @ 309,394: 15x21
#3 @ 655,494: 12x23
#4 @ 298,689: 12x25

Output: number of double-claimed cells e.g.:
3
"""

if __name__ == "__main__":
    input_regex_find = re.compile(r'#\d+ @ (\d+),(\d+): (\d+)x(\d+)')

    claims = dict()
    duplicates = 0
    try:
        while True:
            s = input()
            (left, top, width, height) = re.sub(input_regex_find, r'\1 \2 \3 \4', s).split(' ')
            left = int(left)
            top = int(top)
            width = int(width)
            height = int(height)
            for y in range(0, width):
                for x in range(0, height):
                    coordinates = '{}x{}'.format(top+x, left+y)
                    current_claim_count = claims.get(coordinates)
                    if current_claim_count is None: # New claim
                        claims[coordinates] = 1
                    elif current_claim_count == 1: # Seen once before
                        duplicates += 1
                        claims[coordinates] += 1
                    else: # Triple claim! (Or more than triple.) Already counted as a repeat, so ignore
                        pass
    except EOFError:
        print(duplicates)
        pass
