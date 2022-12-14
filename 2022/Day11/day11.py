import os
import sys
from datetime import datetime

class Monkey:
    def __init__(self, items, operation, test, throw_if_true, throw_if_false) -> None:
        self._items = items
        self._operation = operation
        self._test = test
        self._throw_if_true = throw_if_true
        self._throw_if_false = throw_if_false
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @property
    def items(self):
        return self._items

    @property
    def operation(self):
        return self._operation

    @property
    def test(self):
        return self._test

    @property
    def throw_if_true(self):
        return self._throw_if_true

    @property
    def throw_if_false(self):
        return self._throw_if_false

def run_rounds(monkeys, round):
    pass

def day11_part1(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = None
    print("Day 11 - Part 1 - {}: {}".format(input_name, result))


def day11_part2(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = None
    print("Day 11 - Part 2 - {}: {}".format(input_name, result))


if __name__ == "__main__":

    print("========== Test ==========")
    start = datetime.now()
    day11_part1("test.txt")
    elapsed_time = datetime.now() - start
    print("Part 1 - test: " + str(elapsed_time))
    print("")

    start = datetime.now()
    day11_part2("test.txt")
    elapsed_time = datetime.now() - start
    print("Part 2 - test: " + str(elapsed_time))
    print("")

    print("========== Input ==========")
    start = datetime.now()
    day11_part1("input.txt")
    print("Part 1 - input: " + str(elapsed_time))
    print("")

    start = datetime.now()
    day11_part2("input.txt")
    elapsed_time = datetime.now() - start
    print("Part 2 - input: " + str(elapsed_time))
    print("")
