def open_file(day):
    my_file = open(f"./days/day{day}/input.txt", "r")
    data = my_file.read()
    my_file.close()
    return data
