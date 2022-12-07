import os
import sys
from datetime import datetime

def parse_input_commands(input):
    return [[i for i in line.strip().split("\n")] for line in input.strip().split("$ ")]
    
def directories_under_limit(current_dir, limit):
    if current_dir["_size"] < limit:
        yield current_dir["_size"]
    for k, v in current_dir.items():
        if k != ".." and isinstance(v, dict):
            for i in directories_under_limit(v, limit):
                yield i

def directories_over_limit(current_dir, limit):
    if current_dir["_size"] > limit:
        yield current_dir["_size"]
    for k, v in current_dir.items():
        if k != ".." and isinstance(v, dict):
            for i in directories_over_limit(v, limit):
                yield i


def file_system(input):
    commands = parse_input_commands(input)
    root = {"..": None, "_size": 0}
    current_dir = root
    for command in commands:
        if not command[0]:
            continue
        elif command[0].startswith("cd"):
            dir = command[0][3:]
            if dir == "/":
                current_dir = root
            elif dir == "..":
                current_dir = current_dir.get("..")
            else:
                current_dir[dir] = {"..": current_dir, "_size": 0}
                current_dir = current_dir[dir]
        elif command[0].startswith("ls"):
            for node in command[1:]:
                if node.startswith("dir"):
                    continue
                else:
                    file = node.split(" ")
                    file_size = int(file[0])
                    current_dir[file[1]] = file_size
                    current_dir["_size"] += file_size
                    parent = current_dir[".."]
                    while parent:
                        parent["_size"] += file_size
                        parent = parent.get("..", None)
    return root
    
def get_sum_directories_under_100000(input):
    root = file_system(input)
    return sum(directories_under_limit(root, 100000))

def get_size_of_directory_to_delete(input):
    root = file_system(input)
    free_space = 70000000 - root["_size"]
    delta = 30000000 - free_space
    return min(directories_over_limit(root, delta))

def day07_part1(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = get_sum_directories_under_100000(input)
    print("Day 07 - Part 1 - {}: {}".format(input_name, result))


def day07_part2(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = get_size_of_directory_to_delete(input)
    print("Day 07 - Part 2 - {}: {}".format(input_name, result))


if __name__ == "__main__":

    start = datetime.now()
    day07_part1("test.txt")
    elapsed_time = datetime.now() - start
    print("Part 1 - test: " + str(elapsed_time))
    print("")

    start = datetime.now()
    day07_part2("test.txt")
    elapsed_time = datetime.now() - start
    print("Part 2 - test: " + str(elapsed_time))
    print("")

    start = datetime.now()
    day07_part1("input.txt")
    print("Part 1 - input: " + str(elapsed_time))
    print("")
    
    start = datetime.now()
    day07_part2("input.txt")
    elapsed_time = datetime.now() - start
    print("Part 2 - input: " + str(elapsed_time))
    print("")