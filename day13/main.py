def solve_part_1(input, fold):
    dots = set()
    x = fold[1]
    for coord in input:
        if coord[0] < x:
            dots.add(coord)
        elif coord[0] > x:
            new_dot = (x - (coord[0] - x), coord[1])
            dots.add(new_dot)
    return len(dots)


def solve_part_2(input, folds):
    for axis, num in folds:
        dots = set()
        for x, y in input:
            if axis == "x" and x > num:
                x = num - (x - num)
            elif axis == "y" and y > num:
                y = num - (y - num)

            dots.add((x, y))

        input = dots

    for y in range(6):
        for x in range(39):
            if (x, y) in input:
                print("#", end="")
            else:
                print(" ", end="")
        print()

    return ""


def get_puzzle_input():
    puzzle_input = set()
    folds = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            if line.strip():
                if "fold along y" in line:
                    folds.append(("y", (int(line.strip().split("=")[1]))))
                elif "fold along x" in line:
                    folds.append(("x", (int(line.strip().split("=")[1]))))
                else:
                    coords = line.strip().split(",")
                    puzzle_input.add((int(coords[0]), int(coords[1])))
    return puzzle_input, folds


if __name__ == "__main__":
    puzzle_input, folds = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input, folds[0])
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input, folds)
    print(f"Part 2: {answer_2}")
