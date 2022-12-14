from days import utils

convert_elevation = {}
letters = [*"abcdefghijklmnopqrstuvwxyz"]
for i in range(26):
    convert_elevation[letters[i]] = i + 1


test = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def main():
    elevations_input = utils.open_file(12).split("\n")
    # elevations_input = test.split("\n")
    elevations = []
    start = ()
    end = ()
    # Find start and end, store their coordinates
    # convert letters to numbers so the values are easier to compare
    for i in range(len(elevations_input)):
        new_elevation_row = []
        for j in range(len(elevations_input[i])):
            elevation = elevations_input[i][j]
            if elevation == "S":
                new_elevation_row.append(1)
                start = (i, j)
            elif elevation == "E":
                new_elevation_row.append(26)
                end = (i, j)
            else:
                new_elevation_row.append(convert_elevation[elevation])
        elevations.append(new_elevation_row)
    graph = {}
    # for each elevation, identify neighbors possible to move to, store in form of graph
    for i in range(len(elevations)):
        for j in range(len(elevations[i])):
            coord = (i, j)
            neighbors = []
            if i > 0:
                # check up
                if (elevations[i - 1][j] - elevations[i][j]) < 2:
                    neighbors.append((i - 1, j))
            if i < len(elevations) - 1:
                # check down
                if (elevations[i + 1][j] - elevations[i][j]) < 2:
                    neighbors.append((i + 1, j))
            if j > 0:
                # check left
                if (elevations[i][j - 1] - elevations[i][j]) < 2:
                    neighbors.append((i, j - 1))
            if j < len(elevations[i]) - 1:
                # check right
                if (elevations[i][j + 1] - elevations[i][j]) < 2:
                    neighbors.append((i, j + 1))
            graph[(i, j)] = neighbors
    # BFS to find end
    current = start
    steps = 0
    processed = set()
    queue = [[current]]
    while len(queue) and current != end:
        current_level = queue.pop(0)
        steps += 1
        neighbors_to_add_to_queue = []
        while len(current_level) > 0 and current != end:
            current = current_level.pop(0)
            if current not in processed:
                # process neighbors
                neighbors = graph[current]
                for neighbor in neighbors:
                    if neighbor == end:
                        current = neighbor
                        break
                    if neighbor not in processed:
                        neighbors_to_add_to_queue.append(neighbor)
            processed.add(current)
        queue.append(neighbors_to_add_to_queue)
    print(steps)
