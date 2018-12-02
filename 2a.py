#!/usr/bin/env python3

from functools import reduce

"""
Advent of Code 2018
Puzzle #2 - 2018-12-02: Calculate a checksum
# https://adventofcode.com/2018/day/2


Input (via stdin): A list of IDs. e.g.:
gafljgfajlcwaejlrc
cswavahktrvewagklv

Output: number_of_ids_wherein_at_least_one_character_appears_ecactly_twice * number_of_ids_wherein_at_least_one_character_appears_ecactly_thrice. e.g.:
90210
"""


# This code misses on tri-count: aqcipaizwtnhesagvxjobmkfyr
# Because the tricount is the first letter in the list.
def repeated_count(current=(False, False, '', 0), character=''):
    """ Take an input and try to deterine if it has a character that repeats 2 times and/or 3 times.
    """
    if len(current) == 1:
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


if __name__ == "__main__":
    # My initial solution uses these with reduce using repeated_count:
    di_count = 0
    tri_count = 0

    try:
        while True:
            s = input()
            (exactly_two_seen, exactly_three_seen, last_character, how_many_times_we_saw_last_character) = reduce(repeated_count, (sorted(s)))
            if exactly_two_seen or how_many_times_we_saw_last_character == 2:
                di_count += 1
            if exactly_three_seen or how_many_times_we_saw_last_character == 3:
                tri_count += 1
    except EOFError:
        print(di_count * tri_count)
