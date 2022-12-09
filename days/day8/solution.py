from days import utils


def look(base_height, trees_in_sight):
    num_trees = 0
    for tree in trees_in_sight:
        if tree >= base_height:
            return num_trees + 1
        num_trees += 1
    return num_trees


def count_visible(trees, index, type="row"):
    blocked_height = -1
    total_visible = set()
    for i in range(len(trees)):
        if int(trees[i]) > blocked_height:
            blocked_height = int(trees[i])
            if type == "row":
                total_visible.add(f"{index}-{i}")
            else:
                total_visible.add(f"{i}-{index}")
    blocked_height = -1
    for i in range(len(trees) - 1, 0, -1):
        if int(trees[i]) > blocked_height:
            blocked_height = int(trees[i])
            if type == "row":
                total_visible.add(f"{index}-{i}")
            else:
                total_visible.add(f"{i}-{index}")
    return total_visible


def main():
    input_rows = utils.open_file(8).split("\n")
    trees = []
    for row in input_rows:
        trees.append([*row])
    visible = set()
    # check trees from left to right
    # check trees from right to left
    for i in range(len(trees)):
        visible = visible.union(count_visible(trees[i], i))
    # check trees from top to bottom
    # check trees from bottom to top
    for i in range(len(trees[0])):
        visible = visible.union(count_visible([x[i] for x in trees], i, "col"))
    print("Part 1: ", len(visible))
    highest_score = 0
    for i in range(len(trees)):
        for j in range(len(trees[0])):
            right = look(trees[i][j], trees[i][j + 1 :])
            left = look(trees[i][j], reversed(trees[i][:j]))
            # everything in my column above me
            uplist = []
            for x in range(i - 1, -1, -1):
                uplist.append(trees[x][j])
            up = look(trees[i][j], uplist)
            # everything in my column below me
            downlist = []
            for x in range(i + 1, len(trees)):
                downlist.append(trees[x][j])
            down = look(trees[i][j], downlist)
            score = up * down * right * left
            if score > highest_score:
                highest_score = score
    print("Part 2: ", highest_score)
