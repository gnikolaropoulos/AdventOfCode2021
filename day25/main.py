def solve_part_1(input, height, width):
    cycles = 0
    while True:
        cycles += 1
        new_input = {}
        moved = 0
        for (y,x), cucumber in input.items():
            if cucumber == ">":
                next_x = x+1 if x+1 < width else 0
                if (y, next_x) in input.keys():
                    new_input[y,x] = input[(y,x)]
                    continue
                else:
                    new_input[y, next_x] = ">"
                    moved += 1
            else:
                new_input[(y,x)] = input[(y,x)]
        input = new_input.copy()
        new_input = {}
        for (y, x), cucumber in input.items():
            if cucumber == "v":
                next_y = y + 1 if y + 1 < height else 0
                if (next_y, x) in input.keys():
                    new_input[y,x] = input[(y,x)]
                    continue
                else:
                    new_input[(next_y, x)] = "v"
                    moved += 1
            else:
                new_input[(y,x)] = input[(y,x)]
        input = new_input.copy()

        if moved == 0:
            break

    return cycles

# def solve_part_2(input):
#     pass


def get_puzzle_input():
    puzzle_input = {}
    width = 0
    height = 0
    with open("input.txt") as input_txt:
        for line in input_txt:
            width = len(line.strip())
            for j, char in enumerate(line.strip()):
                if char != ".":
                    puzzle_input[(height,j)]=char
            height += 1

    return puzzle_input, height, width


if __name__ == "__main__":
    puzzle_input, height, width = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input, height, width)
    print(f"Part 1: {answer_1}")

    # answer_2 = solve_part_2(puzzle_input)
    # print(f"Part 2: {answer_2}")
