![banner.png](https://www.digifloor.com/wp-content/uploads/2016/07/python-banner.jpg)

---

#### Repository
https://github.com/python

#### What will I learn

- Findall
- 2D list
- Sets

#### Requirements

- Python 3.7.2
- [Pipenv](https://pypi.org/project/pipenv/)
- git

#### Difficulty

- basic

---

### Tutorial

#### Preface

This tutorial is part of a course where solutions to puzzles from [Advent of Code 2018](https://adventofcode.com/2018/) are discussed to explain programming techniques using Python. Each puzzle contains two parts and comes with user specific inputs. It is recommended to try out the puzzle first before going over the tutorial. Puzzles are a great and fun way to learn about programming.

While the puzzles start of relatively easy and get more difficult over time. Basic programming understanding is required. Such as the different type of variables, lists, dicts, functions and loops etc. A course like [Learn Python2 from Codeacademy](https://www.codecademy.com/learn/learn-python) should be sufficient. Even though the course is for Python two, while Python 3 is used.

This tutorial will look at [puzzle 3](https://adventofcode.com/2018/day/3)

The code for this tutorial can be found on [Github](https://github.com/Juless89/tutorials-aoc)!

#### Part one

> How many square inches of fabric are within two or more claims?

This puzzle comes with a list claims that come with a x, y coordinates and the size of a grid. 

```
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
```

These claims can be plotted in a grid. An `x` represents a field with multiple claims.

```
........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........
```
<br>
> The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

This puzzle can be solved by creating a grid of at least `1000x1000` and going over the claims. Then going over each field to see if there are more than 1 claims.

#### findall

The input for this puzzle is more complicated than seen so far. Te retrieve all the numbers from each line a `regular expression` can be used in combination with `findall()`. A regular expression defines a search pattern, in this case to search for any numbers of any length `r'\d+'` is used. Where `\d` represents a digit and `+` specifies any length, `r` in front of the string makes it a regular expression. More information about regular expressions can be found [here](https://www.guru99.com/python-regular-expressions-complete-tutorial.html).

```
# read input file and convert to list
import re

with open('input.txt', 'r') as file:
    lines = list(file)

    for line in lines:
        id, x, y, w, h = map(int, re.findall(r'\d+', line))
```

#### 2D list

The field can be represented by a two dimensional list. Which is a list of lists. Accessing the list is done by using both indexes. For example `list[x][y]`. Creating the list is done by using a list comprehension. In this example an empty list is set for each field in the grid.

```
# create 2d list of empty lists
field_w, field_h = 1000, 1000
field = [[[] for x in range(field_w)] for y in range(field_h)]
```
<br>
The 2D list is then filled by going over each line from the input. The coordinates for the the fields inside the grid are calculated by taking the start coordinates `x` and `y` and adding the height `h` and width `w` to them.

```
# go over each input line, extracts numbers
# by using a regular expression.
for line in lines:
    id, x, y, w, h = map(int, re.findall(r'\d+', line))

    # use starting coordinates x, y with grid
    # size w, h to add the id to the correct field
    for a in range(y, y + h):
        for b in range(x, x + w):
            field[a][b].append(id)
```

The amount of fields that contain more than one id is calculated by going over each field in the grid.

```
# loop through entire 2d list to count 
# which fields hold more than 1 id
multiple_claims = 0
for a in range(0, field_h):
    for b in range(0, field_h):
        if len(field[a][b]) > 1:
            multiple_claims += 1
```

This can also be achieved with a one liner by using a list comprehension.

```
sum([sum([len(field[x][y]) > 1 for x in range(field_w)]) for y in range(field_h)]))
```
<br>
This list comprehension creates a list with Booleans for each `x` value. From this list the `sum` is taken and put into a list for each `y` value. Again the `sum` is taken returning the `total`. `True` has the value of `1` and `False` of `0` when taking the sum of Booleans.


#### Part two

> What is the ID of the only claim that doesn't overlap?

This puzzle can be solved by using sets. One set that contains `all` the ids and another set that `invalid` ids. That is for  fields that contain more than one id. Subtracting the `invalid` ids set from the `all` ids set results in the `valid` id.

#### Sets

Sets are unordered collections of unique variables. This means that adding a variable to a set that already contains this variable does not expand the set. Also different sets with the same variables but a different order are equal. Furthermore `-` operations work on sets.


![Apr-08-2019 04-33-39.gif](https://cdn.steemitimages.com/DQmUXtbKEsnZTJyo4rHP1QSaqxdDnAwqBU6a6Ztau5AHvSu/Apr-08-2019%2004-33-39.gif)

```
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
```

#### Running the code

Run the code with: `python main.py`

```
if __name__ == "__main__":
    # read input file and convert to list
    with open('input.txt', 'r') as file:
        lines = list(file)

    field = create_field(lines)

    print(f'Part 1 Answer: {part_1(field)}')
    print(f'Part 2 Answer: {part_2(field)}')
```
![Apr-08-2019 04-50-41.gif](https://cdn.steemitimages.com/DQmQjDF8GUirbFaNMcZj3LUmPYDupBu2ZyaTNvPFB26H25h/Apr-08-2019%2004-50-41.gif)

#### Curriculum
[Part 1](https://steemit.com/utopian-io/@steempytutorials/learn-how-to-program-with-python-1---solving-puzzles-from-advent-of-code-2018), [Part 2](https://steemit.com/utopian-io/@steempytutorials/learn-how-to-program-with-python-2---solving-puzzles-from-advent-of-code-2018)

---

The code for this tutorial can be found on [Github](https://github.com/Juless89/tutorials-aoc)!

This tutorial was written by @juliank.