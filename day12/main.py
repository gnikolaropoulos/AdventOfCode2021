from collections import defaultdict


def solve_part_1(graph):
    return traverse(graph, "start", set())


def traverse(graph, node, visited):
    if node == "end":
        return 1

    paths = 0
    next_visited = visited.copy()
    next_visited.add(node)
    for edge in graph[node]:
        if edge in visited and not edge.isupper():
            continue

        paths += traverse(graph, edge, next_visited)

    return paths


def solve_part_2(graph):
    return traverse2(graph, "start", {})


def traverse2(graph, node, visited):
    if node == "end":
        return 1

    paths = 0
    next_visited = visited.copy()
    if node.islower():
        next_visited[node] = next_visited.get(node, 0) + 1

    path_has_double_visited_node = len([v for v in next_visited.values() if v > 1]) > 0

    for edge in graph[node]:
        if edge == "start":
            continue
        elif next_visited.get(edge, 0) >= 1 and path_has_double_visited_node:
            continue

        paths += traverse2(graph, edge, next_visited)

    return paths


def get_puzzle_input():
    graph = defaultdict(set)
    with open("input.txt") as input_txt:
        for line in input_txt:
            nodes = line.strip().split("-")
            graph[nodes[0]].add(nodes[1])
            graph[nodes[1]].add(nodes[0])
    return graph


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
