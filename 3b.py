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

Output: The claim_id of the one claim with no duplicates, e.g.:
1
"""

if __name__ == "__main__":
    input_regex_find = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

    uninfringed_claims = set()
    claims = dict()
    duplicates = 0
    try:
        while True:
            s = input()
            (claim_id, left, top, width, height) = re.sub(input_regex_find, r'\1 \2 \3 \4 \5', s).split(' ')
            # There's probably a more elegant way to do this:
            left = int(left)
            top = int(top)
            width = int(width)
            height = int(height)

            is_uninfringed = True
            for y in range(0, width):
                for x in range(0, height):
                    coordinates = '{}x{}'.format(top+x, left+y)
                    existing_claim = claims.get(coordinates)
                    if existing_claim is None: # New claim
                        claims[coordinates] = claim_id
                    else: # Seen before
                        is_uninfringed = False

                        if existing_claim in uninfringed_claims:
                            # The claim recorded in claims[coordinates] has been infringed upon by the current claim:
                            uninfringed_claims.remove(existing_claim)

                        claims[coordinates] = claim_id

            if is_uninfringed:
                uninfringed_claims.add(claim_id)
    except EOFError:
        print(uninfringed_claims.pop())
