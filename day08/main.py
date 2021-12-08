from collections import defaultdict


def solve_part_1(input):
    count = 0
    for line in input:
        parts = line.split("|")
        outputs = parts[1].strip().split()

        for output in outputs:
            if len(output) == 7 or len(output) == 4 or len(output) == 3 or len(output) == 2:
                count += 1
    return count


def solve_part_2(input):
    digits = defaultdict()
    total_sum = 0
    for line in input:
        parts = line.split("|")
        signals = parts[0].strip().split()
        outputs = parts[1].strip().split()

        for signal in signals:
            if len(signal) == 7:
                digits[8] = sorted(signal)
            if len(signal) == 4:
                digits[4] = sorted(signal)
            if len(signal) == 3:
                digits[7] = sorted(signal)
            if len(signal) == 2:
                digits[1] = sorted(signal)
        for signal in signals:
            if len(signal) == 6:
                if not all(x in signal for x in digits[1]):
                    digits[6] = sorted(signal)
                elif all(x in signal for x in digits[4]):
                    digits[9] = sorted(signal)
                else:
                    digits[0] = sorted(signal)
        for signal in signals:
            if len(signal) == 5:
                if all(x in digits[9] for x in signal) and all(x in digits[6] for x in signal):
                    digits[5] = sorted(signal)
                elif all(x in digits[9] for x in signal):
                    digits[3] = sorted(signal)
                else:
                    digits[2] = sorted(signal)

        output_number = 0
        for output in outputs:
            for digit in digits:
                if sorted(output) == digits[digit]:
                    output_number = output_number * 10 + digit
        total_sum += output_number
    return total_sum


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
