import itertools
import math
from functools import reduce


def solve_part_1(input):
    return magnitude(reduce(add, input))


def add_left(sub_list, num):
    if num is None:
        return sub_list
    if isinstance(sub_list, int):
        return sub_list + num
    return [add_left(sub_list[0], num), sub_list[1]]


def add_right(sub_list, num):
    if num is None:
        return sub_list
    if isinstance(sub_list, int):
        return sub_list + num
    return [sub_list[0], add_right(sub_list[1], num)]


def explode(x, n=4):
    if isinstance(x, int):
        return False, None, x, None
    if n == 0:
        return True, x[0], 0, x[1]
    a, b = x
    exp, left, new_list, right = explode(a, n - 1)
    if exp:
        return True, left, [new_list, add_left(b, right)], None
    exp, left, new_list, right = explode(b, n - 1)
    if exp:
        return True, None, [add_right(a, left), new_list], right
    return False, None, x, None


def split(x):
    if isinstance(x, int):
        if x >= 10:
            return True, [x // 2, math.ceil(x / 2)]
        return False, x
    a, b = x
    change, a = split(a)
    if change:
        return True, [a, b]
    change, b = split(b)
    return change, [a, b]


def add(a, b):
    x = [a, b]
    while True:
        change, _, x, _ = explode(x)
        if change:
            continue
        change, x = split(x)
        if not change:
            break
    return x


def magnitude(x):
    if isinstance(x, int):
        return x
    return 3 * magnitude(x[0]) + 2 * magnitude(x[1])


def solve_part_2(input):
    return max(magnitude(add(a, b)) for a, b in itertools.permutations(input, 2))


def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append((eval(line.strip())))
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
