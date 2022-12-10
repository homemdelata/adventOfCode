import os
import sys
from datetime import datetime

def count_visible_trees(trees_maps):
    pass

def day08_part1(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = count_visible_trees(input)
    print("Day 08 - Part 1 - {}: {}".format(input_name, result))


def day08_part2(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = None
    print("Day 08 - Part 2 - {}: {}".format(input_name, result))


if __name__ == "__main__":

    start = datetime.now()
    day08_part1("test.txt")
    elapsed_time = datetime.now() - start
    print("Part 1 - test: " + str(elapsed_time))
    print("")

    start = datetime.now()
    day08_part2("test.txt")
    elapsed_time = datetime.now() - start
    print("Part 2 - test: " + str(elapsed_time))
    print("")

    start = datetime.now()
    day08_part1("input.txt")
    print("Part 1 - input: " + str(elapsed_time))
    print("")
    
    start = datetime.now()
    day08_part2("input.txt")
    elapsed_time = datetime.now() - start
    print("Part 2 - input: " + str(elapsed_time))
    print("")