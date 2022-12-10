import os
import sys
from datetime import datetime


def parse_trees_map(trees_map_input):
    return [list(map(int, [*line])) for line in trees_map_input.strip().split("\n")]


def get_edge_count(trees_map):
    return (len(trees_map) * 2) + ((len(trees_map[0]) - 2) * 2)


def get_interior_count(trees_map):
    interior_count = 0
    for i in range(1, len(trees_map[1:-1])+1):
        for j in range(1, len(trees_map[0][1:-1])+1):
            top = all(item < trees_map[i][j] for item in [trees_map[top_i][j] for top_i in range(i)])
            right = all(item < trees_map[i][j] for item in [trees_map[i][right_j] for right_j in range(j+1, len(trees_map[0]))])
            bottom = all(item < trees_map[i][j] for item in [trees_map[bottom_i][j] for bottom_i in range(i+1, len(trees_map))])
            left = all(item < trees_map[i][j] for item in [trees_map[i][left_j] for left_j in range(j)])
            if top or right or bottom or left:
                interior_count += 1
    return interior_count


def count_visible_trees(trees_map_input):
    trees_map = parse_trees_map(trees_map_input)
    edge_visible_count = get_edge_count(trees_map)
    interior_visible_count = get_interior_count(trees_map)
    return edge_visible_count + interior_visible_count


def get_higher_viewing_distance(trees_map):
    result = -1
    for i in range(1, len(trees_map[1:-1])+1):
        for j in range(1, len(trees_map[0][1:-1])+1):
            current_tree = trees_map[i][j]
            top = 0
            for item in [trees_map[top_i][j] for top_i in reversed(range(i))]:
                top += 1
                if item >= current_tree:
                    break
                
            right = 0
            for item in [trees_map[i][right_j] for right_j in range(j+1, len(trees_map[0]))]:
                right += 1
                if item >= current_tree:
                    break
                
            bottom = 0
            for item in [trees_map[bottom_i][j] for bottom_i in range(i+1, len(trees_map))]:
                bottom += 1
                if item >= current_tree:
                    break
                
            left = 0
            for item in [trees_map[i][left_j] for left_j in reversed(range(j))]:
                left += 1
                if item >= current_tree:
                    break
                
            viewing_distance = top * right * bottom * left
            if viewing_distance > result:
                result = viewing_distance

    return result


def higher_viewing_distance(trees_map_input):
    trees_map = parse_trees_map(trees_map_input)
    return get_higher_viewing_distance(trees_map)

def day08_part1(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = count_visible_trees(input)
    print("Day 08 - Part 1 - {}: {}".format(input_name, result))


def day08_part2(input_name):
    with open(os.path.join(sys.path[0], input_name), 'r') as file:
        input = file.read()
        result = higher_viewing_distance(input)
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
