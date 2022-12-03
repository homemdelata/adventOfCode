import os
import string
import sys


def parse_rucksacks(input):
    return input.strip().split("\n")


def get_duplicate_item(rucksack):
    half_rucksack = int(len(rucksack)/2)
    first_compartiment = rucksack[:half_rucksack]
    second_compartiment = rucksack[-half_rucksack:]
    return list(set(first_compartiment).intersection(second_compartiment))[0]


def get_item_priority(item):
    priority_list = string.ascii_lowercase[:26] + string.ascii_uppercase[:26]
    return priority_list.index(item) + 1


def sum_priorities(rucksack_list):
    return sum([get_item_priority(get_duplicate_item(rucksack)) for rucksack in rucksack_list])


def create_groups(rucksack_list):
    return [rucksack_list[i:i + 3] for i in range(0, len(rucksack_list), 3)]


def group_badge(elves_group):
    return list(set(elves_group[0]).intersection(elves_group[1]).intersection(elves_group[2]))[0]


def sum_group_priorities(rucksack_list):
    return sum([get_item_priority(group_badge(group)) for group in create_groups(rucksack_list)])


def day03_part1(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = sum_priorities(parse_rucksacks(input))
    print("Day 03 - Part 1 - {}: {}".format(input_name, result))


def day03_part2(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = sum_group_priorities(parse_rucksacks(input))
    print("Day 03 - Part 2 - {}: {}".format(input_name, result))


if __name__ == "__main__":
    day03_part1("test.txt")
    day03_part1("input.txt")

    day03_part2("test.txt")
    day03_part2("input.txt")
