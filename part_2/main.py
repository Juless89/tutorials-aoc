import time

def part_1(lines):
    # store results
    results = {'2': 0, '3': 0}
    
    # go over each line
    for line in lines:
        # store each character's count
        count = {}

        # check if c already in count
        for c in line:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

        # if 2/3 in values, statement is true
        # increment with 1 
        results['2'] += 2 in count.values()
        results['3'] += 3 in count.values()
    
    # return amount of 2s * 3s
    return results['2'] * results['3']

def part_2(lines):

    # loop until lines is empty or answer
    # is found
    while len(lines) > 0:
        # remove line from list
        line1 = lines.pop(0)
    
        # loop through remaining list
        for x in range(0, len(lines)):
            line2 = lines[x]
    
            difference = 0
            # compare each character, for each
            # character that is different add 1
            # to difference
            for c in range(0, len(line1)):
                if line1[c] != line2[c]:
                    difference += 1
    
            # if difference is 1 return id
            if difference == 1:
                return line1

if __name__ == "__main__":
    # read input file and convert to list
    # remove `\n`
    with open('input.txt', 'r') as file:
        lines = [x.strip() for x in file]

    print(f'Part 1 Answer: {part_1(lines)}')
    print(f'Part 2 Answer: {part_2(lines)}')