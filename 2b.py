#!/usr/bin/env python3

"""
Advent of Code 2018
Puzzle #2 - 2018-12-02: Find two strings with hamming distance of one
# https://adventofcode.com/2018/day/2


Input (via stdin): A series of strings. e.g.:
abcdef
hijklm
uvwxyz
azcdef

Output: One of two strings that differ by exactly one character, with the matching character excluded. e.g.:
acdef

"""


def find_id_with_hamming_of_one(ids):
    # We're going to be bad and assume that all IDs are the same length.
    # It's true in our input, but not explicit in the problem statement.
    # We're also just going to bruteforce it in a most horrendous manner:
    for i in range(1, len(list(ids)[0])):
        split_ids = set()
        for id in ids:
            s = id[0:i] + id[i+1:]
            if s in split_ids:
                return s
            split_ids.add(s)


if __name__ == "__main__":
    ids = set()
    try:
        while True:
            ids.add(input())
    except EOFError:
        print(find_id_with_hamming_of_one(ids))