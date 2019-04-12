![banner.png](https://www.digifloor.com/wp-content/uploads/2016/07/python-banner.jpg)

---

#### Repository
https://github.com/python

#### What will I learn

- ASCII values of characters
- Converting a string into a unique set of lowercase characters
- Remove characters from a string

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

This tutorial will look at [puzzle 4](https://adventofcode.com/2018/day/4)

The code for this tutorial can be found on [Github](https://github.com/Juless89/tutorials-aoc)!

#### Puzzle 4

This puzzle is about chemical reactions that are mapped inside a string. Characters react with each other and disappear when they are the same pair, but opposite polarity. Polarity is distinguished by capital and non capital characters. For example aA, bB and cC are pairs with opposite polarity.  

#### Part one

> How many units remain after fully reacting the polymer you scanned? 

A long strong is given, calculating the final length of the string after all pairs have reacted can be done by going over each character and comparing that to the next one. 

```
# read input file and convert to string
with open('input.txt', 'r') as file:
    string = str([x.strip() for x in file][0])
```

#### ASCII values of characters

Every character has a ASCII values, this is how characters can be recognised across operating systems. Characters can be checked to be equal based on their ASCII value. In addition arithmetic can be performed on the ASCII value to transfers the character. For example from a lowercase to an uppercase.

In python `ord()` is used to convert a character into their ASCII value, while `chr()` is used to convert an ASCII values into a character.

`A` has the value of 65 and `a` has a value of 97. There is a 32 difference. Converting an uppercase to a lowercase is done by adding 32 to ASCII value, while converting to a lowercase is done by subtracting 32. A full list can be found [here](https://www.ascii-code.com/)


![Apr-12-2019 19-18-48.gif](https://cdn.steemitimages.com/DQmU4R5ZtcioieTak6hmU51mU1MHVuLq8bsNU6KW42gHf3E/Apr-12-2019%2019-18-48.gif)

```
def part_1(string):
    # filtered characters
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
```
<br>
`filtered` contains all the characters that could not immediately be reacted. For each character `c` in the string, `c2` is the last filtered character `filtered[-1]`. `c2` is checked to not be empty, then the ASCII value is taken from both `c` and `c2` and the difference is checked to be equal to 32. This is done by using `abs()` which return the absolute value.

When the difference is 32, the last filtered character gets removed with `pop()`. If there is no match `c` get added to `filtered`. In the end the string of list is returned, which is the answer to the first part of the puzzle.

Instead of doing the ASCII arithmetic by hand Python has a function `swapcase()` which does the same thing. This leads to the following code:

```
before
if c2 != '' and (abs(ord(c) - ord(c2))) == 32:

after
if c == c2.swapcase():
```

#### Part two

> What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?

Solving this part of the puzzle can be done by reusing the code from the previous part but making one change to the string beforehand. That is, removing all units of exactly one type.

#### Converting a string into a unique set of lowercase characters

Each type consists of a lower and uppercase character. To create a set of all types it is easier to either go for all lowercase or all uppercase. This can be done with `.lower()` or `.upper()`. `Set()` can then be used to take out all the unique characters.

```
def part_2(string):
    # return set off all unique lower case units
    types = set(string.lower())
```

This results in:
```
{'v', 'q', 'z', 'a', 'p', 'k', 'r', 'n', 's', 'j', 'e', 'u', 'h', 'f', 'c', 'm', 'y', 'o', 'g', 'w', 'b', 'x', 'i', 'd', 'l', 't'}
```

This set can now be used to remove all upper and lowercase variants form the input string.

#### Remove characters from a string

Removing characters can be done by using `.replace()` which takes two arguments. The character to be replaced and what to replace the character with. To remove something replacing the character with the empty string `''` does the job.


```
# return min for filtered string where lower and upper case of unit are removed
return (min([part_1(string.replace(t, '').replace(t.upper(), '')) for t in types]))
```

Each character is taken from the set `types` and used to replace that character inside the string for the empty string. To remove the upper case variants `t` is also casted to an uppercase. This is done in a list comprehension that calls the function for `part_1`, which returns the length of the output string. `min()` is taken from this list to return the lowest number.

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
![Screenshot 2019-04-12 at 20.07.42.png](https://cdn.steemitimages.com/DQmUot6Z9JTeFY5D9XRqyijXW7nLnhhyq1Nk4mVjt3xxWXz/Screenshot%202019-04-12%20at%2020.07.42.png)

#### Curriculum
[Part 1](https://steemit.com/utopian-io/@steempytutorials/learn-how-to-program-with-python-1---solving-puzzles-from-advent-of-code-2018), [Part 2](https://steemit.com/utopian-io/@steempytutorials/learn-how-to-program-with-python-2---solving-puzzles-from-advent-of-code-2018), [Part 3](https://steemit.com/utopian-io/@steempytutorials/learn-how-to-program-with-python-3---solving-puzzles-from-advent-of-code-2018), [Part 4](https://steemit.com/utopian-io/@steempytutorials/learn-how-to-program-with-python-4---solving-puzzles-from-advent-of-code-2018)

---

The code for this tutorial can be found on [Github](https://github.com/Juless89/tutorials-aoc)!

This tutorial was written by @juliank.