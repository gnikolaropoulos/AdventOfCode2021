from functools import reduce


def solve_part_1(input):
    width = len(input[0])
    height = len(input)
    lows = []
    for y in range(height):
        for x in range(width):
            current = int(input[y][x])
            left = 10
            if x-1 > -1:
                left = int(input[y][x-1])
            right = 10
            if x+1 < width:
                right = int(input[y][x+1])
            up = 10
            if y-1 > -1:
                up = int(input[y-1][x])
            down = 10
            if y+1 < height:
                down = int(input[y+1][x])
            if current < left and current < right and current < up and current < down:
                lows.append(current)
    print(lows)
    return sum(x+1 for x in lows)


def solve_part_2(input):
    width = len(input[0])
    height = len(input)

    identified = set()
    basins = []

    for y in range(height):
        for x in range(width):
            val = int(input[y][x])
            if val == 9 or (y, x) in identified:
                continue
            basin = {(y, x)}
            frontier = [(y, x)]

            for dy, dx in frontier:
                for ny, nx in neighs_bounded(dy, dx, 0, height - 1, 0, width - 1):
                    nval = int(input[ny][nx])
                    if nval < 9 and (ny, nx) not in basin:
                        basin.add((ny, nx))
                        frontier.append((ny, nx))

            basins.append(len(basin))
            for by, bx in basin:
                identified.add((by, bx))

    basins.sort()
    print(basins)
    return basins[-1]*basins[-2]*basins[-3]


def neighs_bounded(y, x, min_height, max_height, min_width, max_width):
    neighs = []

    if y > min_height:
        neighs.append([y-1, x])

    if y < max_height:
        neighs.append([y+1, x])

    if x > min_width:
        neighs.append([y, x-1])

    if x < max_width:
        neighs.append([y, x+1])

    return neighs


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
