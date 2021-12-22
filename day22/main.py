import re


def solve_part_1(input):
    cubes = {}
    i = 0
    for on, xrange, yrange, zrange in input:
        for x in range(xrange[0], xrange[1] + 1):
            if x > 50 or x < -50:
                continue
            for y in range(yrange[0], yrange[1] + 1):
                if y > 50 or y < -50:
                    continue
                for z in range(zrange[0], zrange[1] + 1):
                    if z > 50 or z < -50:
                        continue
                    cubes[(x, y, z)] = on

        i += 1

    return sum(cubes.values())


def intersection(xrange, yrange, zrange, previous_xrange, previous_yrange, previous_zrange):
    if xrange[0] <= previous_xrange[0] and xrange[1] >= previous_xrange[1] and \
            yrange[0] <= previous_yrange[0] and yrange[1] >= previous_yrange[1] and \
            zrange[0] <= previous_zrange[0] and zrange[1] >= previous_zrange[1]:
        return previous_xrange, previous_yrange, previous_zrange

    if xrange[0] >= previous_xrange[0] and xrange[1] <= previous_xrange[1] and \
            yrange[0] >= previous_yrange[0] and yrange[1] <= previous_yrange[1] and \
            zrange[0] >= previous_zrange[0] and zrange[1] <= previous_zrange[1]:
        return xrange, yrange, zrange

    if xrange[0] > previous_xrange[1] or yrange[0] > previous_yrange[1] or zrange[0] > previous_zrange[1] or \
            xrange[1] < previous_xrange[0] or yrange[1] < previous_yrange[0] or zrange[1] < previous_zrange[0]:
        return [0, 0], [0, 0], [0, 0]

    return [max(xrange[0], previous_xrange[0]), min(xrange[1], previous_xrange[1])], \
           [max(yrange[0], previous_yrange[0]), min(yrange[1], previous_yrange[1])], \
           [max(zrange[0], previous_zrange[0]), min(zrange[1], previous_zrange[1])]


def solve_part_2(input):
    actual_steps = []
    for on, xrange, yrange, zrange in input:
        reduced_steps = []
        if on:
            reduced_steps.append((on, xrange, yrange, zrange))

        for previous_on, previous_xrange, previous_yrange, previous_zrange in actual_steps:
            new_xrange, new_yrange, new_zrange = \
                intersection(xrange, yrange, zrange, previous_xrange, previous_yrange, previous_zrange)

            if new_xrange[0] == new_xrange[1]:
                continue

            reduced_steps.append((not previous_on, new_xrange, new_yrange, new_zrange))

        actual_steps += reduced_steps
    cubes = 0
    for on, xrange, yrange, zrange in actual_steps:
        size = (xrange[1] + 1 - xrange[0]) * (yrange[1] + 1 - yrange[0]) * (zrange[1] + 1 - zrange[0])
        if on:
            cubes += size
        else:
            cubes -= size

    return cubes


def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            match = re.search("x=(-?[0-9]+)..(-?[0-9]+),y=(-?[0-9]+)..(-?[0-9]+),z=(-?[0-9]+)..(-?[0-9]+)", line)
            on = line.startswith("on")
            xrange = sorted((int(match.group(1)), int(match.group(2))))
            yrange = sorted((int(match.group(3)), int(match.group(4))))
            zrange = sorted((int(match.group(5)), int(match.group(6))))
            puzzle_input.append((on, xrange, yrange, zrange))

    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")