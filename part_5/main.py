
def part_1(string):
    filtered = ['']

    # loop over each character inside the string
    # if the next character is the opposite case 
    # discard both characters, else append to result

    for c in string:
        c2 = filtered[-1]

        # check by ASCII values
        if c2 != '' and (abs(ord(c) - ord(c2))) == 32:
            filtered.pop()
        else:
            filtered.append(c)

    # return length of string
    return len(filtered)

def part_2(string):
    # return set off all unique lower case types
    types = set(string.lower())
    # return min for filtered string where lower and upper case of unit are removed
    return (min([part_1(string.replace(t, '').replace(t.upper(), '')) for t in types]))

if __name__ == "__main__":
    # read input file and convert to string
    with open('input.txt', 'r') as file:
        string = str([x.strip() for x in file][0])

    print(f'Part 1 Answer: {part_1(string)}')
    print(f'Part 2 Answer: {part_2(string)}')