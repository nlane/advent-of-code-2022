from days import utils


def main():
    input_str = utils.open_file(4)
    assignments = input_str.split("\n")
    total = 0
    total2 = 0
    for assignment in assignments:
        elf1, elf2 = [i.split("-") for i in assignment.split(",")]
        if int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
            total += 1
        elif int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1]):
            total += 1
    print(total)
    for assignment in assignments:
        elf1, elf2 = [i.split("-") for i in assignment.split(",")]
        if int(elf1[1]) < int(elf2[0]) or int(elf1[0]) > int(elf2[1]):
            continue
        total2 += 1
    print(total2)
