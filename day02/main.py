def solve_part_1(input):
    depth = 0
    horizontal = 0
    for line in input:
        amount = int(line[-1])
        if "forward" in line:
            horizontal += amount
        if "down" in line:
            depth += amount
        if "up" in line:
            depth -= amount
    return depth * horizontal


def solve_part_2(input):
    depth = 0
    horizontal = 0
    aim = 0
    for line in input:
        amount = int(line[-1])
        if "forward" in line:
            horizontal += amount
            depth += amount * aim
        if "down" in line:
            aim += amount
        if "up" in line:
            aim -= amount
    return depth * horizontal


def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(line.strip())
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")