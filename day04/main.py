def solve_part_1(numbers, boards):
    for i in range(5, len(numbers) + 1):
        drawn = set(numbers[:i])

        for board in boards:
            won = False

            for row in board:
                if all(num in drawn for num in row):
                    won = True
                    break

            for x in range(len(board[0])):
                if all(line[x] in drawn for line in board):
                    won = True
                    break

            if won:
                nonwon = 0

                for line in board:
                    for num in line:
                        if num not in drawn:
                            nonwon += int(num)

                return nonwon * int(numbers[i - 1])


def solve_part_2(numbers, boards):
    haswon = set()
    lastwon = -1

    for i in range(5, len(numbers) + 1):
        drawn = set(numbers[:i])

        for j in range(len(boards)):
            if j in haswon:
                continue

            board = boards[j]
            won = False

            for row in board:
                if all(num in drawn for num in row):
                    won = True
                    break

            for x in range(len(board[0])):
                if all(line[x] in drawn for line in board):
                    won = True
                    break

            if won:
                haswon.add(j)
                lastwon = j

        if len(haswon) == len(boards):
            board = boards[lastwon]
            nonwon = 0

            for line in board:
                for num in line:
                    if num not in drawn:
                        nonwon += int(num)

            return nonwon * int(numbers[i - 1])


def get_puzzle_input():
    numbers = []
    boards = []
    board = []

    with open('input.txt') as input_txt:
        for line in input_txt.readlines():
            if not numbers:
                numbers = line.split(',')
                continue
            if not line.strip():
                if board:
                    boards.append(board)
                    board = []
            else:
                board.append(line.split())
        boards.append(board)

    return numbers, boards


if __name__ == "__main__":
    numbers, boards = get_puzzle_input()

    answer_1 = solve_part_1(numbers, boards)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(numbers, boards)
    print(f"Part 2: {answer_2}")
