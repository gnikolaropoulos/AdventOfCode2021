import sys
from collections import Counter, defaultdict


def solve_part_1(input):
    min_cost = sys.maxsize
    counter = Counter(input)
    for num in range(max(input)):
        cost = 0
        for num2, count2 in counter.items():
            cost += abs(num-num2) * count2
        min_cost = cost if cost < min_cost else min_cost
    return min_cost


def solve_part_2(input):
    min_cost = sys.maxsize
    counter = Counter(input)
    for i in range(max(input)):
        cost = 0
        for num, count in counter.items():
            distance = abs(num - i)
            cost += int(count * distance * (distance+1)/2)
            if cost > min_cost:
                break

        min_cost = cost if min_cost > cost else min_cost
    return min_cost


def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input = [int(x) for x in line.strip().split(",")]
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
