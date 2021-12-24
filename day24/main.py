def solve_part_1(input):
    stack = []
    number = [0]*14
    for i in range(14):
        if input[18 * i + 4][-1] == "1":
            stack.append((i, int(input[18 * i + 15][-1])))
        else:
            j, n = stack.pop()
            n += int(input[18 * i + 5][-1])
            if n > 0:
                number[i] = 9
                number[j] = 9 - n
            else:
                number[i] = 9 + n
                number[j] = 9

    return ''.join(map(str, number))


def solve_part_2(input):
    stack = []
    number = [0] * 14
    for i in range(14):
        if input[18 * i + 4][-1] == "1":
            stack.append((i, int(input[18 * i + 15][-1])))
        else:
            j, n = stack.pop()
            n += int(input[18 * i + 5][-1])
            if n > 0:
                number[i] = 1 + n
                number[j] = 1
            else:
                number[i] = 1
                number[j] = 1 - n

    return ''.join(map(str, number))


def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input.append(line.strip().split())
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
