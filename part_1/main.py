def part_1(lines):
    # convert each value to an int
    # return sum
    return sum(map(int, lines))

def part_2(lines):
    # start frequency
    frequency = 0
    frequency_list = [frequency]

    # loop forever
    while True:

        # convert each line to an int
        # add to frequency
        for line in lines:
            frequency += int(line)

            # check if frequency already seen
            if frequency not in frequency_list:
                frequency_list.append(frequency)
            else:
                # break loop with return
                return(frequency)

if __name__ == "__main__":
    # read input file and convert to list
    with open('input.txt', 'r') as file:
        lines = list(file)

    print(f'Part 1 Answer: {part_1(lines)}')
    print(f'Part 2 Answer: {part_2(lines)}')