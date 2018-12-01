#!/usr/bin/env python3

"""
Advent of Code 2018
Puzzle #1 - 2018-12-01: Calibration of Time Turner - Part 2
# https://adventofcode.com/2018/day/1
Our time turner takes us back in 500-year intervals, but it needs calibration. It will tell us as it drifts from true.


Input (via stdin): A series of intergers with leading signs. e.g.:
+2
-3
-1
+1
+2

Output: The first repeat value of the sum. e.g.:
-1 (is total as of second line and again on the forth line)

Note: The input may not result in a repetition. In that case, re-loop over it until it does.
"""


def get_input():
    inputs = []
    try:
        while True:
            i = int(input())
            inputs.append(i)
            yield i
    except EOFError:
        while True:
            for i in inputs:
                yield i


def calc_totals():
    total = 0
    past_totals = set()
    drift = get_input()
    while True:
        total += next(drift)
        if total in past_totals:
            return total
        else:
            past_totals.add(total)


if __name__ == "__main__":
    print(calc_totals())
