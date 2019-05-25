#!/usr/bin/env python3
import sys
import re


def do_all_of_the_things(sleepytimes):
    input_match = re.compile(r'^\[([0-9]{4}-[0-9]{2}-[0-9]{2}) ([0-9]{2}:[0-9]{2})\] (.*)\n')
    guard_re = re.compile(r'Guard #([0-9]+) begins shift')

    current_guard = None
    state_changes = {}
    events = sorted(sys.stdin.readlines())

    for s in events:
        # Parse the input string:
        (date, time, action) = re.sub(input_match, r'\1,\2,\3', s).split(',')
        action = re.sub(guard_re, r'\1', action)

        date = int(date[5:7]) * 100 + int(date[8:10])  # Convert date to int (mmdd)

        # If time 23:xx, enter for midnight tomorrow:
        if time[:3] == '23:':
            time = '00:00'
            date += 1

        if action.isdigit(): # Shift change
            change_state(state_changes, current_guard, date, time, 'end shift')
            current_guard = action
            change_state(state_changes, current_guard, date, time, 'begin shift')
        else: # Falling asleep or awakening
            change_state(state_changes, current_guard, date, time, action)
    return generate_guard_stats(state_changes)


def change_state(state_changes, g, date, time, a):
    if g is None:
        return  # Early record; we don't know who it is on shift. (Actually, is just the first on-shift)
    # print(f'Guard {g} going to {a}')
    if state_changes.get(g) is None:
        state_changes[g] = {}
    if state_changes[g].get(date) is None:
        state_changes[g][date] = {}
    state_changes[g][date][time] = a


def generate_guard_stats(state_changes):
    most_sleepy = None
    how_sleepy_was_the_most_sleepy = 0
    when_most_sleepy = None
    for guard_id, g in state_changes.items():
        state = None
        # print(f'GUARD {guard_id}')
        time_asleep = 0  # Not a %. Hopefully they all serve the same amount of time. ¯\_(ツ)_/¯
        sleepytimes = {}
        for date, d in sorted(g.items()):
            # print(f'Date: {date}')
            state = None
            t = 0
            for new_t, new_state in sorted(d.items()):
                # print(f'{new_t} => {new_state}')
                new_t = int(new_t[3:])

                if state == 'falls asleep':
                    time_asleep += add_sleepytimes(sleepytimes, t, new_t)
                t = new_t
                state = new_state

            # After the final recorded action of the day, if they're still sleeping on duty, assume they slept to 1am.
            if state == 'falls asleep':
                time_asleep += add_sleepytimes(sleepytimes, t, 60)

            state = None

        print(f'Guard #{guard_id} slept for {time_asleep}.')
        if time_asleep > how_sleepy_was_the_most_sleepy:
            most_sleepy = guard_id
            how_sleepy_was_the_most_sleepy = time_asleep
            for k, v in reversed(sorted(sleepytimes.items(), key=lambda m: m[1])):
                when_most_sleepy = k  # Why can't I just slice this reversed dict? I probably can.
                break
    print('----------')
    print('OKAY GOOD')
    print(f'Guard #{most_sleepy} was ever so sleepy, on-duty sleeping for {how_sleepy_was_the_most_sleepy} minutes, most commonly at minute {when_most_sleepy}.')


def add_sleepytimes(sleepytimes, start, end):
    time_asleep = 0
    for m in range(start, end):
        time_asleep += 1
        sleepytimes[m] = sleepytimes.get(m, 0) + 1
    return time_asleep


if __name__ == "__main__":
    sleepytimes = {}
    do_all_of_the_things(sleepytimes)
