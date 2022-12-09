from days import utils


def get_head_coord(direction, head_coord):
    if direction == "D":
        return (head_coord[0], head_coord[1] - 1)
    if direction == "U":
        return (head_coord[0], head_coord[1] + 1)
    if direction == "R":
        return (head_coord[0] + 1, head_coord[1])
    if direction == "L":
        return (head_coord[0] - 1, head_coord[1])
    return head_coord


def get_tail_coord(head_coord, tail_coord):
    distance = (abs(tail_coord[0] - head_coord[0]), abs(tail_coord[1] - head_coord[1]))
    if distance == (1, 1):
        return tail_coord
    # 2 and 1 diff means diagonal move
    if distance == (2, 1) or distance == (1, 2) or distance == (2, 2):
        # move diagonally
        new_x = 0
        new_y = 0
        if head_coord[0] > tail_coord[0]:
            new_x = tail_coord[0] + 1
        else:
            new_x = tail_coord[0] - 1
        if head_coord[1] > tail_coord[1]:
            new_y = tail_coord[1] + 1
        else:
            new_y = tail_coord[1] - 1
        return (new_x, new_y)
    # 2 and 0 diff means lateral move
    elif distance == (2, 0):
        # move either sideways or vertically, positive or negative depending on if H is > or <
        if head_coord[0] > tail_coord[0]:
            return (tail_coord[0] + 1, tail_coord[1])
        else:
            return (tail_coord[0] - 1, tail_coord[1])
    elif distance == (0, 2):
        # move either sideways or vertically, positive or negative depending on if H is > or <
        if head_coord[1] > tail_coord[1]:
            return (tail_coord[0], tail_coord[1] + 1)
        else:
            return (tail_coord[0], tail_coord[1] - 1)
    return tail_coord


def main():
    instructions = utils.open_file(9).split("\n")
    tail_visited = set([(0, 0)])
    tail_coord = (0, 0)
    head_coord = (0, 0)
    for instruction in instructions:
        direction, steps = instruction.split(" ")
        for _ in range(1, int(steps) + 1):
            head_coord = get_head_coord(direction, head_coord)
            tail_coord = get_tail_coord(head_coord, tail_coord)
            tail_visited.add(tail_coord)
    print("Part 1: ", len(tail_visited))
    # Part 2
    knots = []
    tail_9_visited = set()
    for i in range(10):
        knots.append((0, 0))
    for instruction in instructions:
        direction, steps = instruction.split(" ")
        for _ in range(1, int(steps) + 1):
            knots[0] = get_head_coord(direction, knots[0])
            for i in range(1, 10):
                knots[i] = get_tail_coord(knots[i - 1], knots[i])
            tail_9_visited.add(knots[9])
    print("Part 2: ", len(tail_9_visited))
