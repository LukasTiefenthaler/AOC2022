import os

from Days import *


current_day = Day1

input_file = "Input/" + os.path.basename(current_day.__file__.split('.')[0]) + ".txt"


def init():
    with open(input_file, 'r') as f:
        solve(current_day, f.read().splitlines())


def solve(day, _input):
    print(f"Part1: {day.part1(_input)}")
    print(f"Part2: {day.part2(_input)}")


if __name__ == '__main__':
    init()
