def solve_part_1(input):
    first = input[0]
    count = 0
    for depth in input:
        if depth > first:
            count += 1
        first = depth
    return count


def solve_part_2(input):
    sums = []
    for i in range(0, len(input)):
        if i > 1:
            sums.append(input[i] + input[i-1] + input[i-2])
    return solve_part_1(sums)


def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(int(line))
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
