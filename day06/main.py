from collections import Counter


def solve_part_1(input):
    count = Counter(input)

    for i in range(80):
        new_count = Counter()

        for fish, c in count.items():
            if fish == 0:
                new_count[6] += c
                new_count[8] += c
            else:
                new_count[fish - 1] += c

        count = new_count
    return sum(count.values())


def solve_part_2(input):
    count = Counter(input)

    for i in range(256):
        new_count = Counter()

        for fish, c in count.items():
            if fish == 0:
                new_count[6] += c
                new_count[8] += c
            else:
                new_count[fish - 1] += c

        count = new_count
    return sum(count.values())

def get_puzzle_input():
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input = [int(x) for x  in line.strip().split(",")]
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
