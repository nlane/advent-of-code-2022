from days import utils


def all_chars_diff(str):
    unique = set([*str])
    return len(unique) == len(str)


def main():
    buffer = utils.open_file(6)
    for start in range(len(buffer) - 3):
        window = buffer[start : start + 4]
        if all_chars_diff(window):
            print(start + 4)
            break
    for start in range(len(buffer) - 13):
        window = buffer[start : start + 14]
        if all_chars_diff(window):
            print(start + 14)
            break
