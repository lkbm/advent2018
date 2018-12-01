#!/usr/bin/env python3

"""
Advent of Code 2018
Puzzle #1 - 2018-12-01: Calibration of Time Turner - Part 1
# https://adventofcode.com/2018/day/1
Our time turner takes us back in 500-year intervals, but it needs calibration. It will tell us as it drifts from true.

We need to determine total drift.

Input (via stdin): A series of intergers with leading signs. e.g.:
+2
-3
-1
+4

Output: The sum of the input. e.g.:
2
"""

if __name__ == "__main__":
    total = 0
    try:
        while True:
            i = input()
            try:
                total += int(i)
            except ValueError:
                print('Invalid input: {}. Ignoring and continung ever onwards.'.format({}))
    except EOFError:
        print(total)
