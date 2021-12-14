from collections import Counter, defaultdict


def solve_part_1(template, rules):
    for j in range(10):
        new_template = []
        for i in range(0, len(template)):
            if i+1 == len(template):
                break
            pair = template[i] + template[i + 1]
            if pair in rules:
                pair = pair[0] + rules[pair] + pair[1]
            if len(new_template) == 0:
                new_template += pair
            else:
                new_template += pair[1:]
        template = new_template
    counts = Counter(template).most_common()
    return counts[0][1]-counts[-1][1]


def solve_part_2(template, rules):
    pairs = defaultdict(int)
    for i in range(len(template) - 1):
        pair = template[i] + template[i+1]
        pairs[pair] += 1

    for turn in range(40):
        next_pairs = defaultdict(int)
        for pair, count in pairs.items():
            if pair in rules:
                insert = rules[pair]
                next_pairs[pair[0]+insert] += count
                next_pairs[insert+pair[1]] += count
            else:
                next_pairs[pair] += count

        pairs = next_pairs

    letter_counts = defaultdict(int)
    for pair, count in pairs.items():
        letter_counts[pair[1]] += count

    counts = Counter(letter_counts).most_common()
    return counts[0][1] - counts[-1][1]


def get_puzzle_input():
    rules = {}
    template = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            if "->" not in line and line.strip():
                for char in line.strip():
                    template.append(char)
            elif line.strip():
                parts = line.strip().replace(" ", "").split("->")
                rules[parts[0].strip()] = parts[1]
    return template, rules


if __name__ == "__main__":
    template, rules = get_puzzle_input()

    answer_1 = solve_part_1(template, rules)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(template, rules)
    print(f"Part 2: {answer_2}")
