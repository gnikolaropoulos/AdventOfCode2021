import sys
import time
from collections import defaultdict
from heapq import heappush, heappop


def solve_part_1(input):
    start = time.time()
    heap = [((0, 0), 0)]
    location_costs = defaultdict(lambda: sys.maxsize)
    while len(heap) > 0:
        (i,j), current_cost = heappop(heap)
        for neighbor in ((i, j + 1), (i + 1, j)):
            if neighbor not in input:
                continue

            neighbor_cost = current_cost + input[neighbor]
            if neighbor_cost < location_costs[neighbor]:
                location_costs[neighbor] = neighbor_cost
                heappush(heap,(neighbor, neighbor_cost))
    end = time.time()
    print("The time of execution for part1 is :", end-start)
    return location_costs[max(location_costs.keys())]


def solve_part_2(input):
    start = time.time()
    width, height = max(input.keys())
    height += 1
    width += 1

    new_grid = input.copy()
    for dj in range(5):
        for di in range(5):
            risk_increase = dj + di
            if risk_increase == 0:
                continue

            for (i, j), cost in input.items():
                new_cost = cost + risk_increase
                if new_cost > 9:
                    new_cost -= 9
                new_grid[(i + (di * width), j + (dj * height))] = new_cost

    heap = [((0, 0), 0)]
    location_costs = defaultdict(lambda: sys.maxsize)
    while len(heap) > 0:
        (i,  j), current_cost = heappop(heap)
        for neighbor in ((i, j+1), (i, j-1), (i+1, j), (i-1, j)):
            if neighbor not in new_grid:
                continue

            neighbor_cost = current_cost + new_grid[neighbor]
            if neighbor_cost < location_costs[neighbor]:
                location_costs[neighbor] = neighbor_cost
                heappush(heap, (neighbor, neighbor_cost))
    end = time.time()
    print("The time of execution for part2 is :", end - start)
    return location_costs[max(location_costs.keys())]


def get_puzzle_input():
    puzzle_input = {}
    with open("input.txt") as input_txt:
        for j, line in enumerate(input_txt):
            for i, c in enumerate(line.strip()):
                puzzle_input[(i, j)] = int(c)
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
