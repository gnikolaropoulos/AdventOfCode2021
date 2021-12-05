from collections import defaultdict


def solve_part_1(input):
    grid = defaultdict(int)
    for pairs in input:
        x1, y1 = pairs[0]
        x2, y2 = pairs[1]

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[(x1, y)] += 1

        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[(x, y1)] += 1

    return len([v for v in grid.values() if v > 1])


def solve_part_2(input):
    grid = defaultdict(int)
    for pairs in input:
        x1, y1 = pairs[0]
        x2, y2 = pairs[1]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[(x, y1)] += 1
        elif x2 > x1:
            distance = x2 - x1
            ysign = 1 if y2 > y1 else -1
            for i in range(distance + 1):
                grid[(x1 + i, y1 + (i * ysign))] += 1
        else:
            distance = x1 - x2
            ysign = 1 if y2 > y1 else -1
            for i in range(distance + 1):
                grid[(x1 - i, y1 + (i * ysign))] += 1

    return len([v for v in grid.values() if v > 1])


def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            parts = line.strip().split(",")
            x1 = int(parts[0])
            sub_parts = parts[1].strip().split("->")
            y1 = int(sub_parts[0].strip())
            x2 = int(sub_parts[1].strip())
            y2 = int(parts[2])
            puzzle_input.append([(x1, y1), (x2, y2)])

    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
