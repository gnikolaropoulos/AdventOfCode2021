from collections import defaultdict

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]


def solve_part_1(enhancement_algorithm, input, steps, outer=0):
    for step in range(steps):
        min_x = min(x for y, x in input)
        max_x = max(x for y, x in input)
        min_y = min(y for y, x in input)
        max_y = max(y for y, x in input)
        new_image = defaultdict(int)
        for row in range(min_x - 1, max_x + 2):
            for column in range(min_y - 1, max_y + 2):
                scan = ""
                for direction in directions:
                    (new_x, new_y) = (row + direction[0], column + direction[1])
                    scan += str(input[(new_x, new_y)]) if (new_x, new_y) in input else str(outer)

                index = int(scan, 2)
                new_image[(row, column)] = enhancement_algorithm[index]
        input = new_image.copy()

        if enhancement_algorithm[0] == 1 and enhancement_algorithm[-1] == 0:
            outer = (outer + 1) % 2
        elif enhancement_algorithm[0] == 1:
            outer = 1
        else:
            outer = 0

    return sum(v for v in input.values())


def get_puzzle_input():
    puzzle_input = defaultdict(int)
    algorithm = []
    y = 0
    with open("input.txt") as input_txt:
        for line in input_txt:
            if len(algorithm) == 0:
                for char in line.strip():
                    algorithm.append(1 if char == "#" else 0)
                continue
            if line.strip():
                for x in range(len(line.strip())):
                    puzzle_input[(y, x)] = 1 if line[x] == "#" else 0
                y += 1
    return algorithm, puzzle_input


if __name__ == "__main__":
    algorithm, puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(algorithm, puzzle_input, 2)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_1(algorithm, puzzle_input, 50)
    print(f"Part 2: {answer_2}")
