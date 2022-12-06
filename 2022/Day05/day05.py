import os
import sys


def rearrange_crates(crates_stacks, movements):
    pass


def day05_part1(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = None
    print("Day 05 - Part 1 - {}: {}".format(input_name, result))


def day05_part2(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = None
    print("Day 05 - Part 2 - {}: {}".format(input_name, result))


if __name__ == "__main__":
    day05_part1("test.txt")
    day05_part1("input.txt")

    day05_part2("test.txt")
    day05_part2("input.txt")
