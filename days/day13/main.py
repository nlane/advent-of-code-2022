from days import utils
import json
from functools import cmp_to_key


def compare_packets(pack1, pack2):
    for i in range(min(len(pack1), len(pack2))):
        if type(pack1[i]) is int and type(pack2[i]) is int:
            if pack1[i] > pack2[i]:
                return 1
            if pack1[i] < pack2[i]:
                return -1
        if type(pack1[i]) is list and type(pack2[i]) is int:
            res = compare_packets(pack1[i], [pack2[i]])
            if res != 0:
                return res
        if type(pack2[i]) is list and type(pack1[i]) is int:
            res = compare_packets([pack1[i]], pack2[i])
            if res != 0:
                return res
        if type(pack2[i]) is list and type(pack1[i]) is list:
            res = compare_packets(pack1[i], pack2[i])
            if res != 0:
                return res
    # we made it to the end of the loop
    if len(pack1) < len(pack2):
        return -1
    if len(pack2) < len(pack1):
        return 1
    return 0


def main():
    input_str = utils.open_file(13).split("\n\n")
    sum = 0
    input_pt2 = [[[2]], [[6]]]
    for i in range(len(input_str)):
        row = input_str[i]
        str1, str2 = row.split("\n")
        input_pt2 += [json.loads(str1), json.loads(str2)]
        if compare_packets(json.loads(str1), json.loads(str2)) == -1:
            sum += i + 1
    print("Part 1: ", sum)
    sorted_packets = sorted(input_pt2, key=cmp_to_key(compare_packets))
    print(
        "Part 2: ",
        (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1),
    )
