import re
from collections import defaultdict, Counter
from itertools import combinations


def solve_part_1(input):
    sensor_distances = defaultdict(Counter)
    for scanner_id, beacon_coordinates in input.items():
        scanner_distances = sensor_distances[scanner_id]
        for beacon1, beacon2 in combinations(beacon_coordinates, 2):
            distance = (beacon1[0] - beacon2[0]) ** 2 + (beacon1[1] - beacon2[1]) ** 2 + (beacon1[2] - beacon2[2]) ** 2
            scanner_distances[distance] += 1

    paired_scanner_ids = set()
    paired_scanners = []
    for scanner_a, scanner_b in combinations(sensor_distances.keys(), 2):
        distances_a = set(sensor_distances[scanner_a].keys())
        distances_b = set(sensor_distances[scanner_b].keys())
        distances_in_common = distances_a.intersection(distances_b)
        if len(distances_in_common) < 12:
            continue
        paired_scanners.append((scanner_a, scanner_b))
        paired_scanner_ids.add(scanner_a)
        paired_scanner_ids.add(scanner_b)

    normalized_readings = {0: input[0]}
    scanners = [(0, 0, 0)]
    while len(normalized_readings) < len(input):
        for scanner_a, scanner_b in paired_scanners:
            if scanner_a in normalized_readings and scanner_b in normalized_readings:
                continue
            if scanner_a not in normalized_readings and scanner_b not in normalized_readings:
                continue
            if scanner_b in normalized_readings:
                scanner_a, scanner_b = scanner_b, scanner_a

            scanner_b_beacons = input[scanner_b]
            normalized_beacons = normalized_readings[scanner_a]

            candidate_transformations = Counter()
            for beacon in scanner_b_beacons:
                for normalized_beacon in normalized_beacons:
                    for transformed_beacon, rot in all_rotations(beacon):
                        needed_translation = (
                            normalized_beacon[0] - transformed_beacon[0],
                            normalized_beacon[1] - transformed_beacon[1],
                            normalized_beacon[2] - transformed_beacon[2]
                        )

                        candidate_transformations[(rot, needed_translation)] += 1

            (rot, translation), matches = candidate_transformations.most_common(1)[0]
            if matches < 12:
                continue

            scanners.append(translation)

            scanner_b_normalized = []
            for beacon in scanner_b_beacons:
                b = rotate(beacon, rot)
                scanner_b_normalized.append((
                    b[0] + translation[0],
                    b[1] + translation[1],
                    b[2] + translation[2]
                ))

            normalized_readings[scanner_b] = scanner_b_normalized

    beacons = set()
    for readings in normalized_readings.values():
        beacons.update(readings)

    return len(beacons), scanners


def rotate(beacon, rot):
    return (
        beacon[abs(rot[0]) - 1] * (rot[0] // abs(rot[0])),
        beacon[abs(rot[1]) - 1] * (rot[1] // abs(rot[1])),
        beacon[abs(rot[2]) - 1] * (rot[2] // abs(rot[2]))
    )


# https://stackoverflow.com/questions/16452383/how-to-get-all-24-rotations-of-a-3-dimensional-array
def all_rotations(beacon):
    results = []
    for rotation in sequence((1, 2, 3)):
        results.append((rotate(beacon, rotation), rotation))
    return results


def solve_part_2(input):
    largest = 0
    for a, b in combinations(input, 2):
        manhattan_distance = abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
        largest = max(manhattan_distance, largest)

    return largest


def roll(v): return v[0], v[2], -v[1]


def turn(v): return -v[1], v[0], v[2]


def sequence(v):
    for cycle in range(2):
        for step in range(3):
            v = roll(v)
            yield v
            for i in range(3):
                v = turn(v)
                yield v
        v = roll(turn(roll(v)))


def get_puzzle_input():
    puzzle_input = defaultdict(list)
    with open("input.txt") as input_txt:
        current_sensor = None
        for line in input_txt:
            if len(line.strip()) == 0:
                continue
            sensor_match = re.search('scanner ([0-9]+)', line)
            if sensor_match is not None:
                current_sensor = int(sensor_match.group(1))
            else:
                relative_coordinates = tuple(map(int, line.strip().split(",")))
                puzzle_input[current_sensor].append(relative_coordinates)

    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1, scanners = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(scanners)
    print(f"Part 2: {answer_2}")
