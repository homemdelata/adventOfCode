import operator
import os
import sys
from datetime import datetime

def parse_program(program_input):
    lines = [line.split() for line in program_input.strip().split("\n")]
    program = []
    for line in lines:
        command = line[0]
        x = 0
        if len(line) > 1:
            x = int(line[1])
        cycles = 0
        match command:
            case "noop":
                cycles = 1
            case "addx":
                cycles = 2
            case _:
                raise Exception("Command not mapped")
        program.append([command, x, cycles])
    return program

def get_signal_strength_on_cycle(program_input, cycle):
    program = parse_program(program_input)
    x = 1
    i = 0
    running_cycle = 0
    while running_cycle < cycle:
        running_cycle += program[i][2]
        if running_cycle < cycle:
            x += program[i][1]
        i += 1
    return x * cycle

def sum_signal_strengths(program_input, cycles):
    return sum([get_signal_strength_on_cycle(program_input, cycle) for cycle in cycles])
        

def pixel_lit_or_dark(pixel, sprite_position):
    pixel_position = pixel % 40
    if pixel_position >= sprite_position-1 and pixel_position <= sprite_position+1:
        return "#"
    else:
        return "."
    

def get_crt(program_input):
    program = parse_program(program_input)
    x = 1
    total_crt_size = sum([command[2] for command in program])
    pixel_to_draw = 0
    crt = ""
    for command in program:
        match command[0]:
            case "addx":
                crt += pixel_lit_or_dark(pixel_to_draw, x)
                pixel_to_draw += 1
                crt += pixel_lit_or_dark(pixel_to_draw, x)
                pixel_to_draw += 1
                x += command[1]
            case "noop":
                crt += pixel_lit_or_dark(pixel_to_draw, x)
                pixel_to_draw += 1
            case _:
                raise Exception("Command not mapped")
        
    return crt

def draw_crt(crt_line):
    lines = [crt_line[i:i+40] for i in range(0, len(crt_line), 40)]
    for line in lines:
        print(line)

def day10_part1(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = sum_signal_strengths(input, [20, 60, 100, 140, 180, 220])
    print("Day 10 - Part 1 - {}: {}".format(input_name, result))


def day10_part2(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        print("Day 10 - Part 2")
        draw_crt(get_crt(input))


if __name__ == "__main__":

    print("========== Test ==========")
    start = datetime.now()
    day10_part1("test.txt")
    elapsed_time = datetime.now() - start
    print("Part 1 - test: " + str(elapsed_time))
    print("")

    start = datetime.now()
    day10_part2("test.txt")
    elapsed_time = datetime.now() - start
    print("Part 2 - test: " + str(elapsed_time))
    print("")

    print("========== Input ==========")
    start = datetime.now()
    day10_part1("input.txt")
    print("Part 1 - input: " + str(elapsed_time))
    print("")

    start = datetime.now()
    day10_part2("input.txt")
    elapsed_time = datetime.now() - start
    print("Part 2 - input: " + str(elapsed_time))
    print("")
