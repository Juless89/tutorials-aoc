import re

def create_field(lines):
    # create 2d list of empty lists
    field_w, field_h = 1000, 1000
    field = [[[] for x in range(field_w)] for y in range(field_h)]

    # go over each input line, extracts numbers
    # by using a regular expression.
    for line in lines:
        id, x, y, w, h = map(int, re.findall(r'\d+', line))

        # use starting coordinates x, y with grid
        # size w, h to add the id to the correct field
        for a in range(y, y + h):
            for b in range(x, x + w):
                field[a][b].append(id)

    return field

def part_1(field):
    # loop through entire 2d list, check length for each value
    # sum booleans values 
    return sum([sum([len(field[x][y]) > 1 for x in range(len(field))]) for y in range(len(field[0]))])

def part_2(field):
    # sets
    all = set()
    invalid = set()

    # loop through all fields in the grid
    for a in range(0, len(field)):
        for b in range(0, len(field[0])):
            # add each id to all set
            for id in field[a][b]:
                all.add(id)
            # for each field that contains more than
            # 1 id add id to invalid set
            if len(field[a][b]) > 1:
                for id in field[a][b]:
                    invalid.add(id)

    # subtracts invalid ids set from all ids set
    return (all-invalid)

if __name__ == "__main__":
    # read input file and convert to list
    with open('input.txt', 'r') as file:
        lines = list(file)

    field = create_field(lines)

    print(f'Part 1 Answer: {part_1(field)}')
    print(f'Part 2 Answer: {part_2(field)}')