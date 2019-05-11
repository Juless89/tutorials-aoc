![banner.png](https://www.digifloor.com/wp-content/uploads/2016/07/python-banner.jpg)

---

#### Repository
https://github.com/python

#### What will I learn

- Coverting points to coordinate tuples
- Finding the outer bounds of the grid
- Calculating the distance between two locations
- Calculating sum of distances to all locations

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

This tutorial will look at [puzzle 6](https://adventofcode.com/2018/day/6)

The code for this tutorial can be found on [Github](https://github.com/Juless89/tutorials-aoc)!

#### Puzzle 6

The puzzle is about calculating distances between coordinates in an infinite grid.  

#### Part one

A list of coordinates is given which describe locations in a grid. Points in the grid that are closest to these locations belong to that specific location. Points that are equally far from multiple locations are denoted by `.`. Locations are denominated in capital characters while the points belonging to these location are denoted in smaller case characters.

```
aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf
```

<br>
The questions for the first part of the puzzle is:
> What is the size of the largest area that isn't infinite?

Points alongside the edges expand infinitely. So only locations that are enclosed by other locations have a non infinite size. 

#### Coverting points to coordinate tuples

The input for the puzzle comes as a list of points that are separated by a `,`.

```
181, 47
337, 53
331, 40
137, 57
200, 96
```

Reading these from the file, extracting the digits, converting them to digits and creating tuples can be done with a list comprehension.

```
# parse lines into (x, y) tuples
with open('input.txt', 'r') as file:
    points = [tuple(map(int, re.findall(r'\d+', x))) for x in file]
```
<br>
This code is equivalent to:

```
locations = []

for line in file:
    // extract digits
    digits = re.findall(r'\d+', line)

    // convert to int inside tuple
    location = tuple(map(int, digits))

    locations.append(location)
```
<br>
Where `re.findall(r'\d+', line)` extracts all the digits, `map()` applies `int()` to each value extracted and `tuple()` convert the list to a set.

#### Finding the outer bounds of the grid

While the grid is infinite in size the locations are in a finite grid. Calculating the borders of this grid can be done by looking for the `min` and `max` values of both the `x` and `y` coordinates.

```
# find the min / max bounds of all locations
x0, x1 = min(x for x, y in locations), max(x for x, y in locations)
y0, y1 = min(y for x, y in locations), max(y for x, y in locations)
```
<br>
#### Calculating the distance between two locations

To calculate the distance between two locations the [Manhattan distance](https://en.wikipedia.org/wiki/Taxicab_geometry) is given. 

```
# manhattan distance
def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
```
<br>
With the finite grid the distance to each locations from each point inside the grid can be calculated. Each location that has a infinite size has to be discarded. Points that are alongside the borders can be assumed to extend infinitely, the location that they belong to will be discarded. 

```
counts = defaultdict(int)
infinite = set()
```
<br>
The results are stored inside `counts` while infinite locations are stored inside `infinite`.

```
# loop over each point in the finite grid
for y in range(y0, y1 + 1):
    for x in range(x0, x1 + 1):
        # find the distance to each location. Sort result by distance.
        ds = sorted((distance(x, y, px, py), i) for i, (px, py) in enumerate(locations))

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
```
<br>
`for i, (px, py) in enumerate(points)` extracts the coordinates of each location and enumerates the location as `i`. This number is then used to refer back to the location. `(distance(x, y, px, py), i)` then calcuclates the distance to each location and stores this inside a tuple. `sorted` then sorts all the tuples by their first value, which is the distance. 

`if ds[0][0] != ds[1][0]` Looks at the distance from the first and second tuple. When they are not equal there is no tie and the size of the area that it is closest to get increased by 1 `counts[ds[0][1]] += 1`

Points along the border are part of an infinite region and get discarded.

```
return max(counts.values())
```
<br>
Returns the maximum value sorted by the values of the dict.

<center>![May-11-2019 21-23-02.gif](https://cdn.steemitimages.com/DQmR7gkMf51QWCQ9AeS7fR7sU4sPwb3kZzq58AdUUJbxBtA/May-11-2019%2021-23-02.gif)</center>



#### Part two

> What is the size of the region containing all locations which have a total distance to all given coordinates of less than 10000?

The second part of the puzzle is relatively easy. Instead of sorting for the shortest distance take the sum of all distances and check if this value is smaller than 10000 is sufficient. 

#### Calculating sum of distances to all locations

```
counter = 0

# loop over each point in the finite grid
for y in range(y0, y1 + 1):
    for x in range(x0, x1 + 1):
        # calculate distances to each locations and sum all the values
        # if the total value is smaller than 10000 add 1 to the counter
        if sum(distance(x, y, px, py) for px, py in locations) < 10000:
            counter += 1
```
<br>
`sum(distance(x, y, px, py) for px, py in points)` takes the coordinates for each location and calculates the distance from the point to each location. These values are then added together with `sum()`.

<center>![May-11-2019 21-23-30.gif](https://cdn.steemitimages.com/DQmThHZKrGZW2YpXL66JZsecuR2JimWd72xum4qiQhaLaj2/May-11-2019%2021-23-30.gif)</center>

#### Running the code

Run the code with: `python main.py`. This returns both answers for the first and second part of the puzzle. 

```
if __name__ == "__main__":
    # read input file and convert to string
    with open('input.txt', 'r') as file:
        string = str([x.strip() for x in file][0])

    print(f'Part 1 Answer: {part_1(string)}')
    print(f'Part 2 Answer: {part_2(string)}')
```
<br>
<center>![Screenshot 2019-05-11 at 21.25.37.png](https://cdn.steemitimages.com/DQmUgHqeqMnH9QQCTCSDxLCPpgXddvVYCNi1ANZTsvu1L4N/Screenshot%202019-05-11%20at%2021.25.37.png)</center>

#### Curriculum
[Part 1](https://steemit.com/utopian-io/@steempytutorials/learn-how-to-program-with-python-1---solving-puzzles-from-advent-of-code-2018), [Part 2](https://steemit.com/utopian-io/@steempytutorials/learn-how-to-program-with-python-2---solving-puzzles-from-advent-of-code-2018), [Part 3](https://steemit.com/utopian-io/@steempytutorials/learn-how-to-program-with-python-3---solving-puzzles-from-advent-of-code-2018), [Part 4](https://steemit.com/utopian-io/@steempytutorials/learn-how-to-program-with-python-4---solving-puzzles-from-advent-of-code-2018), [Part 5](https://steemit.com/utopian-io/@steempytutorials/-learn-how-to-program-with-python-4---solving-puzzles-from-advent-of-code-2018)

---

The code for this tutorial can be found on [Github](https://github.com/Juless89/tutorials-aoc)!

This tutorial was written by @juliank.