from days import utils

""" 
It's faster to hardcode this part of the input

[J]             [F] [M]            
[Z] [F]     [G] [Q] [F]            
[G] [P]     [H] [Z] [S] [Q]        
[V] [W] [Z] [P] [D] [G] [P]        
[T] [D] [S] [Z] [N] [W] [B] [N]    
[D] [M] [R] [J] [J] [P] [V] [P] [J]
[B] [R] [C] [T] [C] [V] [C] [B] [P]
[N] [S] [V] [R] [T] [N] [G] [Z] [W]
 1   2   3   4   5   6   7   8   9 
"""

crates = [
    ["N", "B", "D", "T", "V", "G", "Z", "J"],
    ["S", "R", "M", "D", "W", "P", "F"],
    ["V", "C", "R", "S", "Z"],
    ["R", "T", "J", "Z", "P", "H", "G"],
    ["T", "C", "J", "N", "D", "Z", "Q", "F"],
    ["N", "V", "P", "W", "G", "S", "F", "M"],
    ["G", "C", "V", "B", "P", "Q"],
    ["Z", "B", "P", "N"],
    ["W", "P", "J"],
]

crates_pt2 = [
    ["N", "B", "D", "T", "V", "G", "Z", "J"],
    ["S", "R", "M", "D", "W", "P", "F"],
    ["V", "C", "R", "S", "Z"],
    ["R", "T", "J", "Z", "P", "H", "G"],
    ["T", "C", "J", "N", "D", "Z", "Q", "F"],
    ["N", "V", "P", "W", "G", "S", "F", "M"],
    ["G", "C", "V", "B", "P", "Q"],
    ["Z", "B", "P", "N"],
    ["W", "P", "J"],
]


def main():
    input_str = utils.open_file(5)
    _, moves_str = input_str.split("\n\n")
    moves = (
        moves_str.replace("from", "").replace("to", "").replace("move ", "").split("\n")
    )
    for move in moves:
        num_crates, from_pile, to_pile, *_ = move.split("  ")
        for i in range(int(num_crates)):
            move_crate = crates[int(from_pile) - 1].pop()
            crates[int(to_pile) - 1].append(move_crate)
    top_crates = ""
    for pile in crates:
        top_crates += pile[-1]
    print("Part 1: ", top_crates)

    # Part 2
    for move in moves:
        num_crates, from_pile, to_pile, *_ = move.split("  ")
        pile = []
        for i in range(int(num_crates)):
            move_crate = crates_pt2[int(from_pile) - 1].pop()
            pile.append(move_crate)
        for i in range(len(pile)):
            crates_pt2[int(to_pile) - 1].append(pile.pop())
    top_crates = ""
    for pile in crates_pt2:
        top_crates += pile[-1]
    print("Part 2: ", top_crates)
