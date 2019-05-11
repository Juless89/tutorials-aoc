from collections import defaultdict
import re


def grid_borders(locations):
    # find the min / max bounds of all points
    x0, x1 = min(x for x, y in locations), max(x for x, y in locations)
    y0, y1 = min(y for x, y in locations), max(y for x, y in locations)

    return x0, x1, y0, y1

# manhattan distance
def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def part_1(locations):
    counts = defaultdict(int)
    infinite = set()

    x0, x1, y0, y1 = grid_borders(locations)

    # loop over each point in the finite grid
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            # find the distance to each location. Sort result by distance.
            ds = sorted((distance(x, y, px, py), i) for i, (px, py) in enumerate(locations))
            print(f'Point: ({x} {y})', end='\r')
            # when the first and second result are not the same there is no tie
            # and the point belongs to a location.
            if ds[0][0] != ds[1][0]:
                counts[ds[0][1]] += 1

                # points along the border are part of an infinite location
                if x == x0 or y == y0 or x == x1 or y == y1:
                    infinite.add(ds[0][1])

    # discard all infinite locations
    for k in infinite:
        counts.pop(k)

    # return the maximal area
    print()
    return max(counts.values())


def part_2(locations):
    x0, x1, y0, y1 = grid_borders(locations)
    counter = 0

    # loop over each point in the finite grid
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            # calculate distances to each locations and sum all the values
            # if the total value is smaller than 10000 add 1 to the counter
            if sum(distance(x, y, px, py) for px, py in locations) < 10000:
                print(f'Point: ({x} {y}) is valid', end='\r')
                counter += 1

    print()
    # return counter
    return(counter)

if __name__ == "__main__":
    # parse lines into (x, y) tuples
    with open('input.txt', 'r') as file:
        locations = [tuple(map(int, re.findall(r'\d+', x))) for x in file]

    print(f'Part 1 Answer: {part_1(locations)}')
    print(f'Part 2 Answer: {part_2(locations)}')
    