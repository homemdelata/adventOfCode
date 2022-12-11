import operator
import os
import sys
from datetime import datetime

def parse_motions(motions_input):
    return [[m[0], int(m[1])] for m in [motion.split() for motion in motions_input.strip().split("\n")]]

def tail_postitions(motions_input):
    motions = parse_motions(motions_input)
    current_head_position = (0, 0)
    current_tail_position = (0, 0)
    list_tail_positions = [current_tail_position]
    for motion in motions:
        head_direction = (0, 0)
        match motion[0]:
            case "U":
                head_direction = (0, 1)
            case "R":
                head_direction = (1, 0)
            case "D":
                head_direction = (0, -1)
            case "L":
                head_direction = (-1, 0)
            case _:
                raise Exception("Motion not mapped")
        
        for i in range(motion[1]):
            current_head_position = tuple(map(operator.add, current_head_position, head_direction))
            delta = tuple(map(operator.sub, current_head_position, current_tail_position))
            if abs(delta[0]) > 1 or abs(delta[1]) > 1:
                x = 0
                y = 0
                if abs(delta[0]) != 0:
                    x = int(delta[0]/abs(delta[0]))
                if abs(delta[1]) != 0:
                    y = int(delta[1]/abs(delta[1]))
                tail_direction = (x, y)
                current_tail_position = tuple(map(operator.add, current_tail_position, tail_direction))
            
            if current_tail_position not in list_tail_positions:
                list_tail_positions.append(current_tail_position)
    
    return len(list_tail_positions)


def day09_part1(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = tail_postitions(input)
    print("Day 09 - Part 1 - {}: {}".format(input_name, result))


def day09_part2(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = None
    print("Day 09 - Part 2 - {}: {}".format(input_name, result))


if __name__ == "__main__":

    print("========== Test ==========")
    start = datetime.now()
    day09_part1("test.txt")
    elapsed_time = datetime.now() - start
    print("Part 1 - test: " + str(elapsed_time))
    print("")

    start = datetime.now()
    day09_part2("test.txt")
    elapsed_time = datetime.now() - start
    print("Part 2 - test: " + str(elapsed_time))
    print("")

    print("========== Input ==========")
    start = datetime.now()
    day09_part1("input.txt")
    print("Part 1 - input: " + str(elapsed_time))
    print("")

    start = datetime.now()
    day09_part2("input.txt")
    elapsed_time = datetime.now() - start
    print("Part 2 - input: " + str(elapsed_time))
    print("")
