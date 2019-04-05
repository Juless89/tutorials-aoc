![banner.png](https://www.digifloor.com/wp-content/uploads/2016/07/python-banner.jpg)

---

#### Repository
https://github.com/python

#### What will I learn

- Workspace
- Virtual environment
- Reading files
- Part one: int(), map(), sum()
- Part two


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

This tutorial will jumpstart the course by going over the basic fundamentals while also explaining the first puzzle of Advent of Code.

#### Setup

Download the files from Github and install the virtual environment

```
$ cd ~/
$ git clone https://github.com/Juless89/tutorials-aoc.git
$ cd tutorials-aoc
$ pipenv install
$ pipenv shell
$ cd part_1
```

#### Workspace

A good code editor is essential for any programmer to be able to work effectively. While there are many different editors this course will be using [Visual Code Studio](https://code.visualstudio.com/). It is not required but highly recommended. A good editor allows for a good overview of the workspace, is dynamic in the sense that addons can be added and comes with error highlighting. Just like Word lets the user know when a word is not spelled correctly an editor will be able to see basic programming errors.

To add the this course go to `File>Open Workspace...` and add the base folder.

![Screenshot-2019-04-05-20.58.29.png](https://cdn.steemitimages.com/DQmctYbBdMLaAftEkjHwRgqj4cJVh2HoS9mi8i7mC52cxq5/Screenshot-2019-04-05-20.58.29.png)


#### Virtual environment

Python comes in different versions and allows for many different packages to be imported. A virtual environment allows the user to keep track and manage these versions and packages without them interfering with each other. This keeps applications isolated from each other, making changes to one virtual environment won't possible corrupt another.

This course will be using `pipenv`.

```
# Linux
pip install pipenv

# mac
brew install pipenv

```

Create a new virtual environment inside a folder with `pipenv install`, enter the virtual environment with `pipenv shell` and exit the virtual evironment with `exit`. An active virtual evironment is highlighted by `(base_folder_)name`.


![Apr-05-2019 21-02-10.gif](https://cdn.steemitimages.com/DQmYUvgWLoDnZfNLkr2b5AaRRxfRwFdddWJUTpbrjDEnqSw/Apr-05-2019%2021-02-10.gif)

#### Reading files

As most of the puzzles come with huge inputs best practise is to separate this into a separate file. For each puzzle the input will be stored inside `input.txt`. When dealing with files the user has to account for closing the file after use and exceptions. This can be simplified by using a `with` statement. "The with statement simplifies exception handling by encapsulating common
preparation and cleanup tasks."

```
file = open('input.txt', 'r')

lines = list(file)

file.close() 
```

Is equal to:

```
# read input file and convert to list
with open('input.txt', 'r') as file:
    lines = list(file)
```
`list()` convert the file to a list.

#### Part one: int(), map(), sum()
For part one of puzzle one a list with frequency changes is given `+1, -2, +3, +1`. Where each input represents a change to the current frequency.

> Starting with a frequency of zero, what is the resulting frequency after all of the changes in frequency have been applied?


The input has been loaded inside `lines`, when printing this to the terminal it looks different.

```
['+3\n',
'+8\n',
'-5\n',
'+15\n',
'+9\n',
'-17\n',
'+11\n']
```

After each input there is a `\n` which represents a new line. In addition `+5` is not a number while `-5` is. Depending on which language the user is using converting these lines to numbers might require additional steps. Luckily Python is quite clever and understands that `+5\n` equals `5`. Converting each line is done by casting them to an int with `int()`.

The most straight forward solution to part 1 would be to loop over all the lines, cast them to an integer and add them to a variable frequency.

```
def part_1(lines):
    frequency = 0

    # convert each line to an int and 
    # add to frequency
    for line in lines:
        frequency += int(line)

    return frequency
```

However, a cleaner and much simpler approach would be to use `sum()`, which returns the total value of all values in a list. For this to work each value needs to be a number though. `int()` is a function, and as such can be used with `map()` to convert each value inside the list to an int. `map()` applies a function to each value of a list.

```
def part_1(lines):
    # convert each value to an int
    # return sum
    return sum(map(int, lines))
```

#### Part two


> You notice that the device repeats the same frequency change list over and over. To calibrate the device, you need to find the first frequency it reaches twice.

Like mentioned in the puzzle the same list gets repeated over and over. And while that is happening the old frequencies have to be stored to know if a frequency is reached twice.

```
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
```

A new variable `frequency_list` is added where all frequencies will be stored in. `while True` will make a loop that lasts forever. 

Each new frequency is compared with the `frequency_list` with `if frequency not in frequency_list:` it gets added if this is not the case with `.append()`. To break out of the `while True` loop the function is set to `return` the frequency that is reached twice. A normal `break` statement would not work in this case.

#### Running the code

Run the code with:

`python main.py`

It takes a while for the 2nd answer to be calculated.

![Screenshot 2019-04-05 20.54.50.png](https://cdn.steemitimages.com/DQmUpLSmtL9X7uL7f2vzkyTTUA9aKSi8BdHgr7RcXmoE62E/Screenshot%202019-04-05%2020.54.50.png)



---

The code for this tutorial can be found on [Github](https://github.com/Juless89/tutorials-websockets)!

This tutorial was written by @juliank.