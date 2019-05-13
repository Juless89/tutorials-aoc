![banner.png](https://www.digifloor.com/wp-content/uploads/2016/07/python-banner.jpg)

---

#### Repository
https://github.com/python

#### What will I learn

- Parsing the input  
- Adding sets (union)
- Comparing sets
- Lexicographical order
- Topological sort

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

This tutorial will look at [puzzle 7](https://adventofcode.com/2018/day/7)

The code for this tutorial can be found on [Github](https://github.com/Juless89/tutorials-aoc)!

#### Puzzle 7

The first part of this puzzle is a topological sort where each step represents a node. As the puzzles are getting more complex this puzzle has been split up into two parts.

#### Part one

A list of requirements is given that dictate which steps are required to be done for a specific step. The goal is determine the order in which the steps have to be completed. When two steps are available based on their requirements the step that is first in alphabetically order has precedence. Steps are indicated with capital characters.

```
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
```
Leads to the following visual representation.

```
  -->A--->B--
 /    \      \
C      -->D----->E
 \           /
  ---->F-----
```

<br>
The questions for the first part of the puzzle is:
> In what order should the steps in your instructions be completed?

#### Parsing the input  

Each line comes with two tasks. Where is second task is the prerequisite for the first task.

```
Step W must be finished before step X can begin.
```
<br>
To solve this puzzle the set of all tasks has to be found and all the prerequisites have to be mapped to their respective task.

```
# set of all task names A - Z
tasks = set()
# maps task to prerequisites
deps = defaultdict(set)
```
<br>
Extracting the tasks can be done with `a, b = re.findall(r' ([A-Z]) ', line)`. Each task is a capital character between A-Z that is surrounded by two whitespaces. These tasks can then be added to the tasks set, and the prerequisite task is mapped to their respective task.
```
with open('input.txt', 'r') as file:
    for line in file:
        a, b = re.findall(r' ([A-Z]) ', line)
        tasks |= {a, b}
        deps[b].add(a)
```


#### Adding sets (union)

In Python adding a set to another set is not done with the `+` operator, instead the `|` operator is used. When using sets this represents the union of two sets.

```
>>>s = {0, 1}
>>>s |= {1, 2}
>>>s

set([0, 1, 2])

>>>s = {0, 1}
>>>s |= {1, 2} | {3, 4}
>>>s

set([0, 1, 2, 3, 4])
```

#### Comparing sets

Sets can be compared with each with more operators than just `==`. A set can be checked to be smaller or larger than another set. A set is only smaller when it is a `subset` of the larger set. This means that all elements contained in the smaller set are also inside the larger set.

```
>>> a = {1,2}
>>> b = {1,2,3}

>>> a > b
False

>>> a < b
True

>>> {4} < b
False

>>> {1} < b
True

>>> {1,4} < b
False
```

#### Lexicographical order

In Python `min()` and `max()` are lexicographic, meaning they are ordered by the alphabet. Casting these functions on a string or list will return the lowest or highest character based on the alphabet.

```
>>> s = ['a', 'f', 'y']

>>> min(s)
'a'
>>> max(s)
'y'
>>> min('afy')
'a'
```

#### Topological sort

Now by combing everything it is possible to solve part 1 of the puzzle. 

```
# store tasks that are done
done = []

for _ in tasks:
    # retrieve the min task that has all prerequisites done
    done.append(min(x for x in tasks if x not in done and prereq[x] <= set(done)))
```
<br>
`x for x in tasks if x not in done and prereq[x] <= set(done)` creates a list of each task that is not in `done` and where the `prereq` set is smaller or equal than the set of all that tasks that are done. `min()` than takes the tasks with the lowest alphabetical order, after which it get's added to the `done` list. `for _ in tasks` makes sure this process is repeated for the amount of tasks, after which it can be assumed that all tasks are done.

```
# return tasks in order as a string
    return ''.join(done)
```

The list is then joined and returned as a string, which is the answer.


#### Running the code

Run the code with: `python main.py`. This returns the answer for part 1 of the puzzle.

```
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
```
<br>
![Screenshot 2019-05-13 at 18.08.55.png](https://cdn.steemitimages.com/DQmWBekP9kEW8Dhec77prRsQ5SBthgZKAdUSukLqEKgGVBE/Screenshot%202019-05-13%20at%2018.08.55.png)

#### Curriculum
[Part 1](https://steemit.com/utopian-io/@steempytutorials/learn-how-to-program-with-python-1---solving-puzzles-from-advent-of-code-2018), [Part 2](https://steemit.com/utopian-io/@steempytutorials/learn-how-to-program-with-python-2---solving-puzzles-from-advent-of-code-2018), [Part 3](https://steemit.com/utopian-io/@steempytutorials/learn-how-to-program-with-python-3---solving-puzzles-from-advent-of-code-2018), [Part 4](https://steemit.com/utopian-io/@steempytutorials/learn-how-to-program-with-python-4---solving-puzzles-from-advent-of-code-2018), [Part 5](https://steemit.com/utopian-io/@steempytutorials/-learn-how-to-program-with-python-4---solving-puzzles-from-advent-of-code-2018), [Part 6](https://steemit.com/utopian-io/@steempytutorials/python-6---advent-of-code-2018---distances-between-points)

---

The code for this tutorial can be found on [Github](https://github.com/Juless89/tutorials-aoc)!

This tutorial was written by @juliank.