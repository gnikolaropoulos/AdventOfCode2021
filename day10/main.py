def solve_part_1(input):
    pairs = {'(': ')', '{': '}', '[': ']', '<': '>'}
    scores = {')': 3, '}': 1197, ']': 57, '>': 25137}
    total_score = 0
    for line in input:
        stack = []
        for char in line:
            if char in pairs.keys():
                stack.append(char)
            else:
                open = stack.pop()
                if pairs[open] == char:
                    continue
                else:
                    total_score += scores[char]
                    break
    return total_score


def solve_part_2(input):
    pairs = {'(': ')', '{': '}', '[': ']', '<': '>'}
    scores = {')': 1, ']': 2, '}': 3, '>': 4}
    total_scores = []
    remaining_stacks = []
    for line in input:
        error = False
        stack = []
        for char in line:
            if char in pairs.keys():
                stack.append(char)
            else:
                open = stack.pop()
                if pairs[open] == char:
                    continue
                else:
                    error = True
                    break
        if error:
            continue
        missing = []
        stack.reverse()
        for c in stack:
            missing.append(pairs[c])
        if len(missing) > 0:
            remaining_stacks.append(missing)
    for stack in remaining_stacks:
        score = 0
        for c in stack:
            score = score * 5 + scores[c]
        total_scores.append(score)
    total_scores.sort()
    return total_scores[int(len(total_scores)/2)]


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
