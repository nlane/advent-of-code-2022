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


def bfs(start, end, graph):
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
    return steps

def bfs_pt2(start, end_val, graph, elevations):
    current = start
    steps = 0
    processed = set()
    queue = [[current]]
    while len(queue) and elevations[current[0]][current[1]] != end_val:
        current_level = queue.pop(0)
        steps += 1
        neighbors_to_add_to_queue = []
        while len(current_level) > 0 and elevations[current[0]][current[1]] != end_val:
            current = current_level.pop(0)
            if current not in processed:
                # process neighbors
                neighbors = graph[current]
                for neighbor in neighbors:
                    if elevations[neighbor[0]][neighbor[1]] == end_val:
                        current = neighbor
                        break
                    if neighbor not in processed:
                        neighbors_to_add_to_queue.append(neighbor)
            processed.add(current)
        queue.append(neighbors_to_add_to_queue)
    return steps



def main():
    elevations_input = utils.open_file(12).split("\n")
    # elevations_input = test.split("\n")
    elevations = []
    start = ()
    end = ()
    hike_starts = []
    # Find start and end, store their coordinates
    # convert letters to numbers so the values are easier to compare
    for i in range(len(elevations_input)):
        new_elevation_row = []
        for j in range(len(elevations_input[i])):
            elevation = elevations_input[i][j]
            if elevation == "S":
                new_elevation_row.append(1)
                start = (i, j)
                hike_starts.append((i, j))
            elif elevation == "E":
                new_elevation_row.append(26)
                end = (i, j)
            else:
                new_elevation_row.append(convert_elevation[elevation])
                if convert_elevation[elevation] == 1:
                    hike_starts.append((i, j))
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
    print("Part 1: ", bfs(start, end, graph))
    graph_pt2 = {}
    # for each elevation, identify neighbors possible to move to, store in form of graph
    for i in range(len(elevations)):
        for j in range(len(elevations[i])):
            coord = (i, j)
            neighbors = []
            if i > 0:
                # check up
                if (elevations[i][j] - elevations[i - 1][j]) < 2:
                    neighbors.append((i - 1, j))
            if i < len(elevations) - 1:
                # check down
                if (elevations[i][j] - elevations[i + 1][j]) < 2:
                    neighbors.append((i + 1, j))
            if j > 0:
                # check left
                if (elevations[i][j] - elevations[i][j - 1]) < 2:
                    neighbors.append((i, j - 1))
            if j < len(elevations[i]) - 1:
                # check right
                if (elevations[i][j] - elevations[i][j + 1]) < 2:
                    neighbors.append((i, j + 1))
            graph_pt2[(i, j)] = neighbors
    print("Part 2: ", bfs_pt2(end, 1, graph_pt2, elevations))
