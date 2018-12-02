#!/usr/bin/env python3

from functools import reduce

"""
Advent of Code 2018
Puzzle #2 - 2018-12-02: Calculate a checksum
# https://adventofcode.com/2018/day/2


Input (via stdin): A list of IDs. e.g.:
gafljgfajlcwaejlrc
cswavahktrvewagklv

Output: number_of_ids_wherein_at_least_one_character_appears_exactly_twice * number_of_ids_wherein_at_least_one_character_appears_exactly_thrice. e.g.:
90210

NOTE: My final code is in 2a.py, but I thought this was interesting. My code in "repeated_count" was missing matches,
and my manually-created test was proving unhelpful in determining why. So instead of test data, I wrote a second
implementation, in the forms of functions "two" and "three", and had both "three" and "repeated_count" return the
string whenever they found a match.
It was then immediately apparent that the oens that "three" found that "repeated_count" didn't were those where the
repeats were the first characters in the (sorted) IDs. e.g., I wasn't identifying "axayaz" because my code for the
initial input, in "if len(current) == 1:" was wrong.

(The quick-and-dirty way I made that code work upon this discover was initially to run the very bad code:
"reduce(repeated_count, (sorted(s + '01')))"

The input was all [a-z], but that wasn't manated by the problem statement, so I hated it, and came back later to fix it.
(I forget exactly what the bad code in "repeated_count" was.
"""


# This code misses on tri-count: aqcipaizwtnhesagvxjobmkfyr
# Because the tricount is the first letter in the list.
def repeated_count(current=(False, False, '', 0), character=''):
    """ Take an input and try to deterine if it has a character that repeats 2 times and/or 3 times.
    """
    if len(current) == 1:
        # This code was wrong, but has since been fixed:
        (exactly_two_seen, exactly_three_seen, last_character_we_looked_at, how_many_times_weve_seen_it_so_far) = (False, False, current, 1)
    else:
        (exactly_two_seen, exactly_three_seen, last_character_we_looked_at, how_many_times_weve_seen_it_so_far) = current
    if last_character_we_looked_at == character:
        how_many_times_weve_seen_it_so_far += 1
    else:
        if how_many_times_weve_seen_it_so_far == 2:
            exactly_two_seen = True
        elif how_many_times_weve_seen_it_so_far == 3:
            exactly_three_seen = True
        how_many_times_weve_seen_it_so_far = 1
    return (exactly_two_seen, exactly_three_seen, character, how_many_times_weve_seen_it_so_far)


# I wrote these as a second implementation in order to compare against the above function:
def two(s):
    chars = {}
    for c in s:
        if chars.get(c):
            chars[c] += 1
        else:
            chars[c] = 1
    
    for v in chars.values():
        if v == 2:
            return 1
    return 0


def three(s):
    chars = {}
    for c in s:
        if chars.get(c):
            chars[c] += 1
        else:
            chars[c] = 1
    
    for v in chars.values():
        if v == 3:
            print(sorted(s))
            print(s)
            return 1
    return 0


if __name__ == "__main__":
    # My initial solution uses these with reduce using repeated_count:
    di_count = 0
    tri_count = 0

    # My "try a different method" solution uses these with the functions "two" and "three".
    d = 0
    t = 0
    try:
        while True:
            s = input()
            # Alt method:
            d += two(s)
            t += three(s)

            # "Real" code:
            (exactly_two_seen, exactly_three_seen, last_character, how_many_times_we_saw_last_character) = reduce(repeated_count, (sorted(s)))
            if exactly_two_seen or how_many_times_we_saw_last_character == 2:
                di_count += 1
            if exactly_three_seen or how_many_times_we_saw_last_character == 3:
                print(s)
                tri_count += 1
    except EOFError:
        print('{} {} {} {}'.format(d, di_count, t, tri_count))
        print(d * t)
        print(di_count * tri_count)
