def solve_part_1(input):
    bit_ones_count = [0] * len(input[0])
    for binary_string in input:
        for i, one_or_zero in enumerate(binary_string):
            bit_ones_count[i] += int(one_or_zero)

    gamma = ""
    epsilon = ""
    for bit in bit_ones_count:
        if bit > (len(input) / 2):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2) * int(epsilon, 2)


def solve_part_2(input):
    oxygen = int(solve(input, 0), 2)
    co2 = int(solve(input, 0, True), 2)

    return oxygen * co2


def solve(input, position, inverted=False):
    if len(input) == 1:
        return "".join(input)
    if position > len(input[0]):
        return "error"
    chars = []
    for line in input:
        chars.append(line[position])
    zeros = count_bits(chars, "0")
    ones = count_bits(chars, "1")
    freq = "1"
    if inverted:
        freq = "0"
    if zeros > ones:
        freq = "0"
        if inverted:
            freq = "1"
    next_input = []
    for line in input:
        if line[position] == freq:
            next_input.append(line)
    return solve(next_input, position+1, inverted)


def count_bits(line, bit):
    count = 0
    for char in line:
        if char == bit:
            count += 1
    return count


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
