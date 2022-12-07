from days import utils


class TreeNode:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.files = []  # tuples (filename, size)
        self.dirs = []  # other tree nodes


def total_file_size(node):
    if node == None:
        return 0
    total = 0
    for file in node.files:
        total += file[1]
    for child_dir in node.dirs:
        total += total_file_size(child_dir)
    return total


def file_sizes_under_100000(node):
    if node == None:
        return 0
    dir_size = total_file_size(node)
    if dir_size > 100000:
        dir_size = 0
    for child in node.dirs:
        dir_size += file_sizes_under_100000(child)
    return dir_size


def all_dir_sizes(node):
    file_size = [total_file_size(node)]
    if node.dirs == []:
        return file_size
    else:
        for child_dir in node.dirs:
            file_size += all_dir_sizes(child_dir)
        return file_size


def main():
    commands = utils.open_file(7).split("\n")
    root = TreeNode(None, "/")
    currNode = root
    for line in commands:
        if line[0:4] == "$ cd":
            cd_loc = line[5:]
            if cd_loc == "/":
                currNode = root
            if cd_loc == "..":
                currNode = currNode.parent
            else:
                for child in currNode.dirs:
                    if child.name == cd_loc:
                        currNode = child
                        break
        if line[0:4] == "$ ls":
            pass
        if line[0] != "$":
            if line[0:3] == "dir":
                currNode.dirs.append(TreeNode(currNode, line[4:]))
            else:
                size, name = line.split(" ")
                currNode.files.append((name, int(size)))
    print("Part 1: ", file_sizes_under_100000(root))
    unused_space = 70000000 - total_file_size(root)
    needed_space = 30000000 - unused_space
    all_dirs = all_dir_sizes(root)
    minimum_size = 70000000
    for dir_size in all_dirs:
        if dir_size < minimum_size and dir_size >= needed_space:
            minimum_size = dir_size
    print("Part 2: ", minimum_size)
