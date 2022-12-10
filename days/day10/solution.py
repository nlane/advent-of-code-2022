from days import utils


def update_cursor(screen_i, screen_j):
    if screen_j in [39, 79, 119, 159, 199, 239]:
        screen_j = 0
        screen_i += 1
    else:
        screen_j += 1
    return (screen_i, screen_j)


def get_pixel(x, screen_j):
    if screen_j in [x - 1, x, x + 1]:
        return "#"
    else:
        return "."


def update_notable_cycles(notable_cycle_signals, cycle, x):
    if cycle in [20, 60, 100, 140, 180, 220]:
        notable_cycle_signals.append(x * cycle)


def main():
    instructions = utils.open_file(10).split("\n")
    notable_cycle_signals = []
    cycle = 1
    x = 1
    screen = [["" for j in range(40)] for i in range(6)]
    screen_i = 0
    screen_j = 0
    for instruction in instructions:
        if screen_i == 6:
            break
        instruction_type = instruction[:4]
        screen[screen_i][screen_j] = get_pixel(x, screen_j)
        screen_i, screen_j = update_cursor(screen_i, screen_j)
        update_notable_cycles(notable_cycle_signals, cycle, x)
        if instruction_type == "addx":
            value = instruction.split(" ")[1]
            cycle += 1
            screen[screen_i][screen_j] = get_pixel(x, screen_j)
            screen_i, screen_j = update_cursor(screen_i, screen_j)
            update_notable_cycles(notable_cycle_signals, cycle, x)
            x += int(value)
        cycle += 1
    print("Part 1: ", sum(notable_cycle_signals))
    for line in screen:
        print("".join(line))
