import os
import string
import sys


def parse_pairs_list(input):
    return [[list(map(int, section.split("-"))) for section in pair.split(",")] for pair in input.strip().split("\n")]


def fully_contains(pair):
    first_section = pair[0]
    second_section = pair[1]
    if first_section[0] <= second_section[0] and first_section[1] >= second_section[1]:
        return True
    elif second_section[0] <= first_section[0] and second_section[1] >= first_section[1]:
        return True
    return False


def count_fully_contained(groups):
    return list(map(fully_contains, groups)).count(True)


def overlaps(pair):
    pass


def count_overlaps(groups):
    pass


def day04_part1(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = count_fully_contained(parse_pairs_list(input))
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
