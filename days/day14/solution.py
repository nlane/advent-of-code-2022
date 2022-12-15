from days import utils

test = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""


def sand_falling_loc(coords, bottom, pt2=False):
    current = (500, 0)
    blocked = False
    while not blocked:
        # if current is out of bounds return None
        if current[1] > bottom:
            if not pt2:
                return None
            else:
                blocked = True
                break
        if (current[0], current[1] + 1) not in coords:
            current = (current[0], current[1] + 1)
            continue
        if (current[0] - 1, current[1] + 1) not in coords:
            current = (current[0] - 1, current[1] + 1)
            continue
        if (current[0] + 1, current[1] + 1) not in coords:
            current = (current[0] + 1, current[1] + 1)
            continue
        blocked = True
    return current


def main():
    input_str = utils.open_file(14).split("\n")
    # input_str = test.split("\n")
    rock_locs = set()
    bottom = 0
    for row in input_str:
        coords = row.split("->")
        for i in range(1, len(coords)):
            startx, starty = [int(loc) for loc in coords[i - 1].split(",")]
            endx, endy = [int(loc) for loc in coords[i].split(",")]
            if startx == endx:
                # the changing y value coords need to be filled in
                if starty < endy:
                    while starty <= endy:
                        if starty > bottom:
                            bottom = starty
                        rock_locs.add((startx, starty))
                        starty += 1
                else:
                    while endy <= starty:
                        if endy > bottom:
                            bottom = endy
                        rock_locs.add((startx, endy))
                        endy += 1
            else:
                # the changing x value coords need to be filled in
                if starty > bottom:
                    bottom = starty
                if startx < endx:
                    while startx <= endx:
                        rock_locs.add((startx, starty))
                        startx += 1
                else:
                    while endx <= startx:
                        rock_locs.add((endx, starty))
                        endx += 1
    rock_locs_pt2 = rock_locs.copy()
    sand = 0
    while True:
        sand_loc = sand_falling_loc(rock_locs, bottom)
        if sand_loc is None:
            break
        rock_locs.add(sand_loc)
        sand += 1
    print(sand)
    sand = 0
    while True:
        sand_loc = sand_falling_loc(rock_locs_pt2, bottom, True)
        if sand_loc == (500, 0):
            sand += 1
            break
        rock_locs_pt2.add(sand_loc)
        sand += 1
    print(sand)
