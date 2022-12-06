import os
import sys
import re
from datetime import datetime


class Plan:
    def __init__(self) -> None:
        self._stacks = []
        self._movements = []

    @property
    def stacks(self):
        return self._stacks

    @stacks.setter
    def stacks(self, stacks):
        self._stacks = stacks

    @property
    def movements(self):
        return self._movements

    @movements.setter
    def movements(self, mvmts):
        self._movements = mvmts


class Movement:
    def __init__(self, movement_string) -> None:
        m = re.match(
            r"move (?P<quantity>\d+) from (?P<source>\d+) to (?P<destiny>\d+)", movement_string)
        self._quantity = int(m["quantity"])
        self._source = int(m["source"])
        self._destiny = int(m["destiny"])

    @property
    def quantity(self):
        return self._quantity

    @property
    def source(self):
        return self._source

    @property
    def destiny(self):
        return self._destiny


def parse_crates(crates_input):
    lines = [[line[i:i+4].strip("[ ]") for i in range(0, len(line), 4)]
             for line in crates_input.split("\n")]
    stacks = [[lines[j][i] for j in reversed(
        range(len(lines)-1)) if lines[j][i] != ""] for i in range(len(lines[0]))]
    return stacks


def parse_movements(movements_input):
    return [Movement(line) for line in movements_input.strip().split("\n")]


def parse_plan(input):
    parsed_input = input.split("\n\n")
    plan = Plan()
    plan.stacks = parse_crates(parsed_input[0])
    plan.movements = parse_movements(parsed_input[1])
    return plan


def rearrange_crates(crates_stacks, movements):
    for movement in movements:
        crates_to_move = crates_stacks[movement.source - 1][-movement.quantity:]
        crates_to_move.reverse()
        crates_stacks[movement.destiny - 1] += crates_to_move
        del crates_stacks[movement.source - 1][-movement.quantity:]
    return "".join([stack[-1:][0] for stack in crates_stacks])


def rearrange_crates_with_new_crane(crates_stacks, movements):
    for movement in movements:
        crates_to_move = crates_stacks[movement.source - 1][-movement.quantity:]
        crates_stacks[movement.destiny - 1] += crates_to_move
        del crates_stacks[movement.source - 1][-movement.quantity:]
    return "".join([stack[-1:][0] for stack in crates_stacks])


def day05_part1(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        plan = parse_plan(input)
        result = rearrange_crates(plan.stacks, plan.movements)
    print("Day 05 - Part 1 - {}: {}".format(input_name, result))


def day05_part2(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        plan = parse_plan(input)
        result = rearrange_crates_with_new_crane(plan.stacks, plan.movements)
    print("Day 05 - Part 2 - {}: {}".format(input_name, result))


if __name__ == "__main__":

    start = datetime.now()
    day05_part1("test.txt")
    elapsed_time = datetime.now() - start
    print("Part 1 - test: " + str(elapsed_time))
    print("")

    start = datetime.now()
    day05_part2("test.txt")
    elapsed_time = datetime.now() - start
    print("Part 2 - test: " + str(elapsed_time))
    print("")

    start = datetime.now()
    day05_part1("input.txt")
    print("Part 1 - input: " + str(elapsed_time))
    print("")
    
    start = datetime.now()
    day05_part2("input.txt")
    elapsed_time = datetime.now() - start
    print("Part 2 - input: " + str(elapsed_time))
    print("")

#    start = datetime.now()
#    day05_part1("aoc_2022_day05_large_input.txt")
#    elapsed_time = datetime.now() - start
#    print("Part 1 - input grande: " + str(elapsed_time))
#    print("")
#
#    start = datetime.now()
#    day05_part2("aoc_2022_day05_large_input.txt")
#    elapsed_time = datetime.now() - start
#    print("Part 2 - input grande: " + str(elapsed_time))
#    print("")
#
#    start = datetime.now()
#    day05_part1("aoc_2022_day05_large_input-2.txt")
#    elapsed_time = datetime.now() - start
#    print("Part 1 - input muito grande: " + str(elapsed_time))
#    print("")
#
#    start = datetime.now()
#    day05_part2("aoc_2022_day05_large_input-2.txt")
#    elapsed_time = datetime.now() - start
#    print("Part 2 - input muito grande: " + str(elapsed_time))
#    print("")

