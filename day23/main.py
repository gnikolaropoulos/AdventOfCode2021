from heapq import heappush, heappop
from itertools import permutations


def scorepos(j, pos):
    score = 0

    for i, yx in enumerate(pos):
        y, x = yx

        if x == 3 + j * 2:
            score += abs(y - (i + 2)) * 10 ** j
        else:
            score += (y - 1 + abs(x - (3 + j * 2)) + i + 1) * 10 ** j

    return score


def heuristic(apos, bpos, cpos, dpos):
    count = 0
    allpos = [apos, bpos, cpos, dpos]

    for j, pos in enumerate(allpos):
        count += min(scorepos(j, p) for p in permutations(pos))

    return count


def bfs(open, start):
    d = {start: []}
    frontier = [[start]]

    for path in frontier:
        node = path[-1]
        y, x = node

        for dy, dx in neighs(y, x):
            if (dy, dx) in open and (dy, dx) not in d:
                d[(dy, dx)] = path + [(dy, dx)]
                frontier.append(path + [(dy, dx)])

    return d


def get_paths(open):
    return {a: bfs(open, a) for a in open}


def neighs(y, x):
    return [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]


def solve_part_1(lines):
    height = len(lines)
    width = len(lines[0])

    a = []
    b = []
    c = []
    d = []

    open = set()

    for y in range(height):
        for x in range(width):
            if lines[y][x] == 'A':
                a.append((y, x))
            if lines[y][x] == 'B':
                b.append((y, x))
            if lines[y][x] == 'C':
                c.append((y, x))
            if lines[y][x] == 'D':
                d.append((y, x))
            if lines[y][x] != '#':
                open.add((y, x))

    blocking = {(1, 3), (1, 5), (1, 7), (1, 9)}
    goala = [(2, 3), (3, 3)]
    goalb = [(2, 5), (3, 5)]
    goalc = [(2, 7), (3, 7)]
    goald = [(2, 9), (3, 9)]

    a.sort()
    b.sort()
    c.sort()
    d.sort()

    states = [[0, a, b, c, d]]
    seen = {(tuple(a), tuple(b), tuple(c), tuple(d)): 0}

    def tuplify(apos, bpos, cpos, dpos):
        return (tuple(apos), tuple(bpos), tuple(cpos), tuple(dpos))

    def isfree(y, x, apos, bpos, cpos, dpos):
        if (y, x) not in open:
            return False
        if (y, x) in apos:
            return False
        if (y, x) in bpos:
            return False
        if (y, x) in cpos:
            return False
        return (y, x) not in dpos

    while True:
        energy, apos, bpos, cpos, dpos = heappop(states)
        allpos = [apos, bpos, cpos, dpos]

        if apos == goala and bpos == goalb and cpos == goalc and dpos == goald:
            return energy

        blocker = False

        for i, yx in enumerate(apos):
            y, x = yx
            if (y, x) in blocking:
                blocker = True
                for deltax in (-1, 1):
                    if isfree(y, x + deltax, apos, bpos, cpos, dpos):
                        if i == 0:
                            dapos = sorted([(y, x + deltax), apos[1]])
                        else:
                            dapos = sorted([(y, x + deltax), apos[0]])
                        t = tuplify(dapos, bpos, cpos, dpos)
                        if t not in seen or seen[t] > energy + 1:
                            seen[t] = energy + 1
                            heappush(states, [energy + 1, dapos, list(bpos), list(cpos), list(dpos)])
                if x == 3 and isfree(2, 3, apos, bpos, cpos, dpos):
                    if not isfree(3, 3, apos, bpos, cpos, dpos) and not (3, 3) in apos:
                        continue
                    if i == 0:
                        dapos = sorted([(2, 3), apos[1]])
                    else:
                        dapos = sorted([(2, 3), apos[0]])
                    t = tuplify(dapos, bpos, cpos, dpos)
                    if t not in seen or seen[t] > energy + 1:
                        seen[t] = energy + 1
                        heappush(states, [energy + 1, list(dapos), list(bpos), list(cpos), list(dpos)])
        for i, yx in enumerate(bpos):
            y, x = yx
            if (y, x) in blocking:
                blocker = True
                for deltax in (-1, 1):
                    if isfree(y, x + deltax, apos, bpos, cpos, dpos):
                        if i == 0:
                            dbpos = sorted([(y, x + deltax), bpos[1]])
                        else:
                            dbpos = sorted([(y, x + deltax), bpos[0]])
                        t = tuplify(apos, dbpos, cpos, dpos)
                        if t not in seen or seen[t] > energy + 10:
                            seen[t] = energy + 10
                            heappush(states, [energy + 10, list(apos), dbpos, list(cpos), list(dpos)])
                if x == 5 and isfree(2, 5, apos, bpos, cpos, dpos):
                    if not isfree(3, 5, apos, bpos, cpos, dpos) and not (3, 5) in bpos:
                        continue
                    if i == 0:
                        dbpos = sorted([(2, 5), bpos[1]])
                    else:
                        dbpos = sorted([(2, 5), bpos[0]])
                    t = tuplify(apos, dbpos, cpos, dpos)
                    if t not in seen or seen[t] > energy + 10:
                        seen[t] = energy + 10
                        heappush(states, [energy + 10, list(apos), list(dbpos), list(cpos), list(dpos)])
        for i, yx in enumerate(cpos):
            y, x = yx
            if (y, x) in blocking:
                blocker = True
                for deltax in (-1, 1):
                    if isfree(y, x + deltax, apos, bpos, cpos, dpos):
                        if i == 0:
                            dcpos = sorted([(y, x + deltax), cpos[1]])
                        else:
                            dcpos = sorted([(y, x + deltax), cpos[0]])
                        t = tuplify(apos, bpos, dcpos, dpos)
                        if t not in seen or seen[t] > energy + 100:
                            seen[t] = energy + 100
                            heappush(states, [energy + 100, list(apos), list(bpos), dcpos, list(dpos)])
                if x == 7 and isfree(2, 7, apos, bpos, cpos, dpos):
                    if not isfree(3, 7, apos, bpos, cpos, dpos) and not (3, 7) in cpos:
                        continue
                    if i == 0:
                        dcpos = sorted([(2, 7), cpos[1]])
                    else:
                        dcpos = sorted([(2, 7), cpos[0]])
                    t = tuplify(apos, bpos, dcpos, dpos)
                    if t not in seen or seen[t] > energy + 100:
                        seen[t] = energy + 100
                        heappush(states, [energy + 100, list(apos), list(bpos), list(dcpos), list(dpos)])
        for i, yx in enumerate(dpos):
            y, x = yx
            if (y, x) in blocking:
                blocker = True
                for deltax in (-1, 1):
                    if isfree(y, x + deltax, apos, bpos, cpos, dpos):
                        if i == 0:
                            ddpos = sorted([(y, x + deltax), dpos[1]])
                        else:
                            ddpos = sorted([(y, x + deltax), dpos[0]])
                        t = tuplify(apos, bpos, cpos, ddpos)
                        if t not in seen or seen[t] > energy + 1000:
                            seen[t] = energy + 1000
                            heappush(states, [energy + 1000, list(apos), list(bpos), list(cpos), ddpos])
                if x == 9 and isfree(2, 9, apos, bpos, cpos, dpos):
                    if not isfree(3, 9, apos, bpos, cpos, dpos) and not (3, 9) in dpos:
                        continue
                    if i == 0:
                        ddpos = sorted([(2, 9), dpos[1]])
                    else:
                        ddpos = sorted([(2, 9), dpos[0]])
                    t = tuplify(apos, bpos, cpos, ddpos)
                    if t not in seen or seen[t] > energy + 1000:
                        seen[t] = energy + 1000
                        heappush(states, [energy + 1000, list(apos), list(bpos), list(cpos), list(ddpos)])

        if blocker:
            continue

        if apos != goala:
            for i in range(2):
                for dy, dx in neighs(apos[i][0], apos[i][1]):
                    if (dy, dx) not in open:
                        continue
                    if any((dy, dx) in pos for pos in allpos):
                        continue
                    if (dy, dx) == (2, 3) and (apos[i][0], apos[i][1]) == (3, 3):
                        continue
                    if (dy, dx) == (2, 5) and (apos[i][0], apos[i][1]) != (3, 5):
                        continue
                    if (dy, dx) == (2, 7) and (apos[i][0], apos[i][1]) != (3, 7):
                        continue
                    if (dy, dx) == (2, 9) and (apos[i][0], apos[i][1]) != (3, 9):
                        continue
                    dapos = []
                    if i == 0:
                        dapos = sorted([(dy, dx), apos[1]])
                    else:
                        dapos = sorted([(dy, dx), apos[0]])
                    t = tuplify(dapos, bpos, cpos, dpos)
                    if t not in seen or seen[t] > energy + 1:
                        seen[t] = energy + 1
                        heappush(states, [energy + 1, list(dapos), list(bpos), list(cpos), list(dpos)])
        if bpos != goalb:
            for i in range(2):
                for dy, dx in neighs(bpos[i][0], bpos[i][1]):
                    if (dy, dx) not in open:
                        continue
                    if any((dy, dx) in pos for pos in allpos):
                        continue
                    if (dy, dx) == (2, 3) and (bpos[i][0], bpos[i][1]) != (3, 3):
                        continue
                    if (dy, dx) == (2, 5) and (bpos[i][0], bpos[i][1]) == (3, 5):
                        continue
                    if (dy, dx) == (2, 7) and (bpos[i][0], bpos[i][1]) != (3, 7):
                        continue
                    if (dy, dx) == (2, 9) and (bpos[i][0], bpos[i][1]) != (3, 9):
                        continue
                    if i == 0:
                        dbpos = sorted([(dy, dx), bpos[1]])
                    else:
                        dbpos = sorted([(dy, dx), bpos[0]])
                    t = tuplify(apos, dbpos, cpos, dpos)
                    if t not in seen or seen[t] > energy + 10:
                        seen[t] = energy + 10
                        heappush(states, [energy + 10, list(apos), list(dbpos), list(cpos), list(dpos)])
        if cpos != goalc:
            for i in range(2):
                for dy, dx in neighs(cpos[i][0], cpos[i][1]):
                    if (dy, dx) not in open:
                        continue
                    if any((dy, dx) in pos for pos in allpos):
                        continue
                    if (dy, dx) == (2, 3) and (cpos[i][0], cpos[i][1]) != (3, 3):
                        continue
                    if (dy, dx) == (2, 5) and (cpos[i][0], cpos[i][1]) != (3, 5):
                        continue
                    if (dy, dx) == (2, 7) and (cpos[i][0], cpos[i][1]) == (3, 7):
                        continue
                    if (dy, dx) == (2, 9) and (cpos[i][0], cpos[i][1]) != (3, 9):
                        continue
                    if i == 0:
                        dcpos = sorted([(dy, dx), cpos[1]])
                    else:
                        dcpos = sorted([(dy, dx), cpos[0]])
                    t = tuplify(apos, bpos, dcpos, dpos)
                    if t not in seen or seen[t] > energy + 100:
                        seen[t] = energy + 100
                        heappush(states, [energy + 100, list(apos), list(bpos), list(dcpos), list(dpos)])
        if dpos != goald:
            for i in range(2):
                for dy, dx in neighs(dpos[i][0], dpos[i][1]):
                    if (dy, dx) not in open:
                        continue
                    if any((dy, dx) in pos for pos in allpos):
                        continue
                    if (dy, dx) == (2, 3) and (dpos[i][0], dpos[i][1]) != (3, 3):
                        continue
                    if (dy, dx) == (2, 5) and (dpos[i][0], dpos[i][1]) != (3, 5):
                        continue
                    if (dy, dx) == (2, 7) and (dpos[i][0], dpos[i][1]) != (3, 7):
                        continue
                    if (dy, dx) == (2, 9) and (dpos[i][0], dpos[i][1]) == (3, 9):
                        continue
                    if i == 0:
                        ddpos = sorted([(dy, dx), dpos[1]])
                    else:
                        ddpos = sorted([(dy, dx), dpos[0]])
                    t = tuplify(apos, bpos, cpos, ddpos)
                    if t not in seen or seen[t] > energy + 1000:
                        seen[t] = energy + 1000
                        heappush(states, [energy + 1000, list(apos), list(bpos), list(cpos), list(ddpos)])


def solve_part_2(lines):
    height = len(lines)
    width = len(lines[0])

    a = []
    b = []
    c = []
    d = []

    open = set()

    for y in range(height):
        for x in range(width):
            if lines[y][x] == 'A':
                a.append((y, x))
            if lines[y][x] == 'B':
                b.append((y, x))
            if lines[y][x] == 'C':
                c.append((y, x))
            if lines[y][x] == 'D':
                d.append((y, x))
            if lines[y][x] not in ' #':
                open.add((y, x))

    paths = get_paths(open)

    blocking = {(1, 3), (1, 5), (1, 7), (1, 9)}

    a.sort()
    b.sort()
    c.sort()
    d.sort()

    def tuplify(apos, bpos, cpos, dpos):
        return (tuple(apos), tuple(bpos), tuple(cpos), tuple(dpos))

    def isfree(y, x, apos, bpos, cpos, dpos):
        if (y, x) not in open:
            return False
        if (y, x) in apos:
            return False
        if (y, x) in bpos:
            return False
        if (y, x) in cpos:
            return False
        return (y, x) not in dpos

    states = [[heuristic(a, b, c, d), 0, a, b, c, d]]
    seen = {(tuple(a), tuple(b), tuple(c), tuple(d)): 0}

    while True:
        h, energy, apos, bpos, cpos, dpos, = heappop(states)

        allpos = [apos, bpos, cpos, dpos]
        occupied = set(apos) | set(bpos) | set(cpos) | set(dpos)

        if h == energy:
            return energy

        def explore(pos, i, j, y, x, steps):
            dpos = sorted(pos[:j] + [(y, x)] + pos[j + 1:])
            dapos, dbpos, dcpos, ddpos = allpos[:i] + [dpos] + allpos[i + 1:]
            t = tuplify(dapos, dbpos, dcpos, ddpos)
            neweng = energy + steps * (10 ** i)

            if t not in seen or seen[t] > neweng:
                seen[t] = neweng
                dh = heuristic(dapos, dbpos, dcpos, ddpos)
                heappush(states, [dh + neweng, neweng, dapos, dbpos, dcpos, ddpos])

        def cango(y1, x1, y2, x2):
            for dy, dx in paths[(y1, x1)][(y2, x2)][1:]:
                if (dy, dx) in occupied:
                    return False

            return True

        for i, pos in enumerate(allpos):
            rightcol = 3 + 2 * i

            for j, yx in enumerate(pos):
                y, x = yx

                if y > 1:
                    cangoup = True
                    hasotherbelow = False
                    hasclearturn = isfree(1, x - 1, apos, bpos, cpos, dpos) or isfree(1, x + 1, apos, bpos, cpos, dpos)

                    if not hasclearturn:
                        continue

                    for gy in range(1, y):
                        if not isfree(gy, x, apos, bpos, cpos, dpos):
                            cangoup = False

                    if not cangoup:
                        continue

                    for gy in range(y + 1, 6):
                        for gpos in [allpos[k] for k in range(len(allpos)) if k != i]:
                            if (gy, x) in gpos:
                                hasotherbelow = True
                                break

                    if x == rightcol and not hasotherbelow:
                        continue

                    for gx in range(1, 12):
                        if (1, gx) in blocking:
                            continue

                        if cango(y, x, 1, gx):
                            explore(pos, i, j, 1, gx, len(paths[(y, x)][(1, gx)]) - 1)
                else:
                    hasotheratgoal = False

                    for gy in range(2, 6):
                        for gpos in [allpos[k] for k in range(len(allpos)) if k != i]:
                            if (gy, rightcol) in gpos:
                                hasotheratgoal = True
                                break

                    if hasotheratgoal:
                        continue

                    for gy in range(5, 1, -1):
                        if cango(y, x, gy, rightcol):
                            explore(pos, i, j, gy, rightcol, len(paths[(y, x)][(gy, rightcol)]) - 1)
                            break


def get_puzzle_input():
    width = -1
    puzzle_input = []
    with open("input.txt") as input_txt:
        for line in input_txt:
            if width == -1:
                width = len(line.rstrip())

            row = line.rstrip()
            row += ' ' * (width - len(row))
            puzzle_input.append(row)
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")
    extra1 = '  #D#C#B#A#  '
    extra2 = '  #D#B#A#C#  '
    puzzle_input.insert(3, extra1)
    puzzle_input.insert(4, extra2)
    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
