import math
import os
import sys
from datetime import datetime

class Monkey:
    def __init__(self, items, operation, test, throw_if_true, throw_if_false) -> None:
        self._items = items
        self._operation = operation
        self._test = test
        self._divisor = int(self._test.replace("divisible by ", ""))
        self._throw_if_true = throw_if_true
        self._throw_if_false = throw_if_false
        self._inspections = 0

    def __eq__(self, other):
        return self.items == other.items and self.operation == other.operation and self.test == other.test and self.throw_if_true == other.throw_if_true and self.throw_if_false == other.throw_if_false

    def inspect(self, item):
        self._inspections += 1
        new_item = eval(self._operation.replace("new = ","").replace("old", str(item)))
        new_item = int(math.floor(new_item / 3))
        new_monkey = self.throw_if_false
        if new_item % self._divisor == 0:
            new_monkey = self.throw_if_true
        return (new_item, new_monkey)

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
    
    @property
    def inspections(self):
        return self._inspections


def parse_monkeys(monkeys_input):
    monkeys_string = [a.split("\n") for a in monkeys_input.strip().split("\n\n")]
    monkeys = []
    for monkey_string in monkeys_string:
        starting_items = [int(item) for item in monkey_string[1].strip().replace("Starting items: ","").split(",")]
        operation = monkey_string[2].strip().replace("Operation: ","")
        test = monkey_string[3].strip().replace("Test: ","")
        throw_if_true = int(monkey_string[4].strip().replace("If true: throw to monkey ",""))
        throw_if_false = int(monkey_string[5].strip().replace("If false: throw to monkey ",""))
        monkeys.append(Monkey(starting_items, operation, test, throw_if_true, throw_if_false))
    return monkeys


def run_rounds(monkeys, rounds):
    for round in range(rounds):
        for monkey in monkeys:
            for i in range(len(monkey.items)):
                item = monkey.items.pop(0)
                inspected_item = monkey.inspect(item)
                monkeys[inspected_item[1]].items.append(inspected_item[0])
    return monkeys


def calculate_monkey_business(monkeys):
    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort()
    return inspections[-1] * inspections[-2]


def part1(monkeys_input):
    monkeys = parse_monkeys(monkeys_input)
    monkeys = run_rounds(monkeys, 20)
    return calculate_monkey_business(monkeys)


def day11_part1(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = part1(input)
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
