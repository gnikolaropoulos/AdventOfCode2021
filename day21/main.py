import re
from collections import Counter
from itertools import product


def solve_part_1(input):
    roll_count = 0
    p1_score = 0
    p2_score = 0
    p1_position = input[0]
    p2_position = input[1]
    roll_die = deterministic_roll()
    while True:
        # Player 1
        p1_score, p1_position, roll_count = play(p1_position, p1_score, roll_count, roll_die)
        if p1_score >= 1000:
            return p2_score * roll_count

        # Player 2
        p2_score, p2_position, roll_count = play(p2_position, p2_score, roll_count, roll_die)
        if p2_score >= 1000:
            return p1_score * roll_count


def play(position, score, roll_count, roll_die):
    roll = next(roll_die) + next(roll_die) + next(roll_die)
    position = (position + roll - 1) % 10 + 1
    score += position
    roll_count += 3
    return score, position, roll_count


def deterministic_roll():
    i = 1
    while True:
        yield i
        i = (i % 100) + 1


def solve_part_2(input):
    size = 10
    moves = 3
    dsize = 3
    rolls = Counter()

    for p in product(range(1, dsize + 1), repeat=moves):
        rolls[sum(p)] += 1

    return max(count(input[0], input[1], 0, 0, True, size, rolls))


def count(p1_position, p2_position, p1_score, p2_score, is_p1_rolling, size, rolls):
    seen = {}
    if p1_score > 20:
        return 1, 0
    if p2_score > 20:
        return 0, 1

    tup = (p1_position, p2_position, p1_score, p2_score, is_p1_rolling)

    if tup in seen:
        return seen[tup]

    p1_wins = 0
    p2_wins = 0

    if is_p1_rolling:
        for score, times in rolls.items():
            next_p1_position = p1_position + score
            if next_p1_position > size:
                next_p1_position -= size
            wins1, wins2 = count(next_p1_position, p2_position, p1_score + next_p1_position, p2_score, False, size, rolls)
            p1_wins += times * wins1
            p2_wins += times * wins2
    else:
        for score, times in rolls.items():
            next_p2_position = p2_position + score
            if next_p2_position > size:
                next_p2_position -= size
            wins1, wins2 = count(p1_position, next_p2_position, p1_score, p2_score + next_p2_position, True, size, rolls)
            p1_wins += times * wins1
            p2_wins += times * wins2

    seen[tup] = (p1_wins, p2_wins)

    return p1_wins, p2_wins


def get_puzzle_input():
    puzzle_input = []
    with open("testinput.txt") as input_txt:
        for line in input_txt:
            player_match = re.search('Player ([0-9]+) starting position: ([0-9]+)', line)
            puzzle_input.append(int(player_match.group(2)))
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
