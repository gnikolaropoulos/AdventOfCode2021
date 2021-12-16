from functools import reduce


def solve_part_1(input):
    return parse_packet(input)[0]


def solve_part_2(input):
    return parse_packet(input)[2]


def parse_packet(packet):
    version = int(packet[0:3], 2)
    version_sum = version
    type_id = int(packet[3:6], 2)
    cursor = 6
    value = 0
    if type_id == 4:
        literal_end = False
        value_bits = ""
        while not literal_end:
            literal_end = packet[cursor] == "0"
            value_bits += packet[cursor + 1:cursor + 5]
            cursor += 5

        value = int(value_bits, 2)

    else:
        length_type_id = packet[6]
        cursor += 1
        subpackets_info = []
        if length_type_id == "0":
            total_subpackets_length = int(packet[7:7 + 15], 2)
            cursor += 15
            packet_end = cursor + total_subpackets_length
            while cursor < packet_end:
                subpacket_info = parse_packet(packet[cursor:])
                subpackets_info.append(subpacket_info)
                subpacket_version_sum, subpacket_length, _ = subpacket_info
                cursor += subpacket_length
                version_sum += subpacket_version_sum

        elif length_type_id == "1":
            cursor += 11
            num_subpackets = int(packet[7:7 + 11], 2)
            for _ in range(num_subpackets):
                subpacket_info = parse_packet(packet[cursor:])
                subpackets_info.append(subpacket_info)
                subpacket_version_sum, subpacket_length, _ = subpacket_info
                cursor += subpacket_length
                version_sum += subpacket_version_sum

        subpacket_values = [info[2] for info in subpackets_info]
        if type_id == 0:
            value = sum(subpacket_values)

        if type_id == 1:
            value = reduce(lambda x, y: x * y, subpacket_values)

        if type_id == 2:
            value = min(subpacket_values)

        if type_id == 3:
            value = max(subpacket_values)

        if type_id == 5:
            value = 1 if subpacket_values[0] > subpacket_values[1] else 0

        if type_id == 6:
            value = 1 if subpacket_values[0] < subpacket_values[1] else 0

        if type_id == 7:
            value = 1 if subpacket_values[0] == subpacket_values[1] else 0

    return version_sum, cursor, value


def get_puzzle_input():
    puzzle_input = ""
    with open("input.txt") as input_txt:
        for line in input_txt:
            puzzle_input = format(int(line.strip(), 16), f'0>{len(line.strip()) * 4}b')
            # for hex in line.strip():
            #     binary = bin(int(hex, 16))[2:]
            #     padding = '0' * (4 - len(binary))
            #     for c in padding + binary:
            #         puzzle_input += c
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = get_puzzle_input()

    answer_1 = solve_part_1(puzzle_input)
    print(f"Part 1: {answer_1}")

    answer_2 = solve_part_2(puzzle_input)
    print(f"Part 2: {answer_2}")
