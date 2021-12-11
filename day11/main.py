def solve_part_1(grid):
    total_flashes = 0
    moment = 0
    for i in range(400):
        flashed = set()
        for key in grid:
            grid[key] += 1

        for key in grid:
            try_flash(key, grid, flashed)

        for k, v in grid.items():
            if v > 9:
                grid[k] = 0
        if i < 100:
            total_flashes += len(flashed)
        if len(grid) == len(flashed):
            moment = i + 1
            break

    return total_flashes, moment


def neighbors(coord, grid):
    x, y = coord
    for xd in (-1, 0, 1):
        for yd in (-1, 0, 1):
            if xd == 0 and yd == 0:
                continue
            c = x + xd, y + yd
            if c in grid:
                yield c


def try_flash(key, grid, flashed):
    if grid[key] <= 9 or key in flashed:
        return

    flashed.add(key)

    for n in neighbors(key, grid):
        grid[n] += 1
        try_flash(n, grid, flashed)


def get_puzzle_input():
    puzzle_input = {}
    with open("input.txt") as input_txt:
        for y, line in enumerate(input_txt):
            for x, c in enumerate(line.strip()):
                puzzle_input[x, y] = int(c)

    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1, answer_2 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    # answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
