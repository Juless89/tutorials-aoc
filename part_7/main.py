from collections import defaultdict
import re


def part_1(tasks, prereq):
    # store tasks that are done
    done = []

    for _ in tasks:
        # retrieve the min task that has all prerequisites done
        done.append(min(x for x in tasks if x not in done and prereq[x] <= set(done)))

    # return tasks in order as a string
    return ''.join(done)


if __name__ == "__main__":
    tasks = set()
    prereq = defaultdict(set)

    with open('input.txt', 'r') as file:
        for line in file:
            # set of all task names A - Z
            a, b = re.findall(r' ([A-Z]) ', line)
            tasks |= {a, b}

            # map task to prerequisites
            prereq[b].add(a)

    print(f'Part 1 Answer: {part_1(tasks, prereq)}')