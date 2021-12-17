import re


def solve_part_1(min_x, max_x, min_y, max_y):
    highest = 0
    count = 0
    for dx in range(1, max_x + 1):
        for dy in range(min_y, 300):
            x, y = 0, 0
            velocity_x = dx
            velocity_y = dy
            current_highest = 0
            success = False
            while x <= max_x and y >= min_y:
                x, y = x + velocity_x, y + velocity_y
                velocity_x = max(0, velocity_x - 1)
                velocity_y -= 1
                current_highest = max(current_highest, y)
                if min_x <= x <= max_x and min_y <= y <= max_y:
                    success = True
            if success:
                count += 1
                highest = max(highest, current_highest)
    return highest, count


def solve_part_2(input):
    pass


def ints(line):
    pattern = re.compile(r'-?\d+')

    return [int(val) for val in re.findall(pattern, line) if val]


def get_puzzle_input():
    x1, x2, y1, y2 = (0, 0, 0, 0)
    with open("input.txt") as input_txt:
        for line in input_txt:
            x1, x2, y1, y2 = ints(line)
    return x1, x2, y1, y2


if __name__ == "__main__":
    min_x, max_x, min_y, max_y = get_puzzle_input()

    answer_1, answer_2 = solve_part_1(min_x, max_x, min_y, max_y)
    print(f"Part 1: {answer_1}")

    # answer_2 = solve_part_2(min_x, max_x, min_y, max_y)
    print(f"Part 2: {answer_2}")
