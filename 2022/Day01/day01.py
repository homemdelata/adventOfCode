
import os
import sys


def parse_elves(input):
    str_elves = [elf.split("\n") for elf in input.strip().split("\n\n")]
    return [list(map(int, i)) for i in str_elves]


def calculate_total_calories(elf):
    return sum(elf)


def day01_part1(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input_test = file.read()
        elves = parse_elves(input_test)
        elves_calories = list(map(calculate_total_calories, elves))
        highest_calories = max(elves_calories)
    print("Day 01 - Part 1 - {}: {}".format(input_name, highest_calories))


def day01_part2(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input_test = file.read()
        elves = parse_elves(input_test)
        elves_calories = list(map(calculate_total_calories, elves))
        elves_calories.sort()
        top3_calories = sum(elves_calories[-3:])
    print("Day 01 - Part 2 - {}: {}".format(input_name, top3_calories))


if __name__ == "__main__":
    day01_part1('test.txt')
    day01_part1('input.txt')

    day01_part2('test.txt')
    day01_part2('input.txt')
