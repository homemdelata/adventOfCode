import os
import string
import sys

def fully_contains(fisrt_section, second_section):
    pass

def count_fully_contained(groups):
    pass

def day04_part1(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = None
    print("Day 04 - Part 1 - {}: {}".format(input_name, result))


def day04_part2(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = None
    print("Day 04 - Part 2 - {}: {}".format(input_name, result))


if __name__ == "__main__":
    day04_part1("test.txt")
    day04_part1("input.txt")

    day04_part2("test.txt")
    day04_part2("input.txt")
