from collections import defaultdict
from operator import itemgetter

import re


def parse_input():
    # totals holds the total amount of minutes a guard has spent sleeping
    # frequency holds the frequency per minute (0-59) for each guard 
    totals = defaultdict(int)
    frequency = defaultdict(lambda: defaultdict(int))

    # read input file and convert to list
    with open('input.txt', 'r') as file:
        lines = list(file)

    # sort lines by timestamp
    for line in sorted(lines):
        # parse minute
        minute = int(re.search(r':(\d+)', line).group(1))
        if '#' in line:
            guard = int(re.search(r'#(\d+)', line).group(1))
        # guards falls asleep, minute included
        elif 'asleep' in line:
            start = minute
        # guard wakes up, minute not included
        elif 'wakes' in line:
            end = minute 

            # for each minute add to totals and frequency
            for m in range(start, end):
                totals[guard] += 1
                frequency[guard][m] += 1

    return totals, frequency

def part_1(totals, frequency):
    key = itemgetter(1) 

    # retrieve guard id sorted by max total minutes asleep
    guard = max(totals.items(), key=key)[0]

    # retrieve minute for which the guard was asleep the most
    minute = max(frequency[guard].items(), key=key)[0]

    return guard * minute

def part_2(frequency):
    items = []
    key = itemgetter(1) 

    # for each guard retrieve the minute with the highest
    # frequency. Store freq and score (guard * minute)
    for guard in frequency:
        minute, freq = max(frequency[guard].items(), key=key)
        items.append((freq, guard * minute))

    # return by highest frequency 
    return sorted(items)[-1][1]

if __name__ == "__main__":
    # parse input into totals and frequency dicts
    totals, frequency = parse_input()

    print(f'Part 1 Answer: {part_1(totals, frequency)}')
    print(f'Part 2 Answer: {part_2(frequency)}')