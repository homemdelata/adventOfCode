from collections import Counter
import os
import sys
from datetime import datetime


def get_starter_marker(message):
    bla = [message[i:i+4] for i in range(len(message))]
    ble = [i for i in range(len(bla)) if len(set(bla[i])) == 4]
    return ble[0] + 4

def get_starter_message(message):
    bla = [message[i:i+14] for i in range(len(message))]
    ble = [i for i in range(len(bla)) if len(set(bla[i])) == 14]
    return ble[0] + 14


def day06_part1(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = get_starter_marker(input)
    print("Day 06 - Part 1 - {}: {}".format(input_name, result))


def day06_part2(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = get_starter_message(input)
    print("Day 06 - Part 2 - {}: {}".format(input_name, result))


if __name__ == "__main__":

    start = datetime.now()
    day06_part1("test.txt")
    elapsed_time = datetime.now() - start
    print("Part 1 - test: " + str(elapsed_time))
    print("")

    start = datetime.now()
    day06_part2("test.txt")
    elapsed_time = datetime.now() - start
    print("Part 2 - test: " + str(elapsed_time))
    print("")

    start = datetime.now()
    day06_part1("input.txt")
    print("Part 1 - input: " + str(elapsed_time))
    print("")
    
    start = datetime.now()
    day06_part2("input.txt")
    elapsed_time = datetime.now() - start
    print("Part 2 - input: " + str(elapsed_time))
    print("")