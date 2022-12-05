def main():
    my_file = open("./days/day1/input.txt", "r")
    data = my_file.read()
    my_file.close()

    data_into_list = data.split("\n\n")
    most_calories = 0
    max_cal_inventory = []

    for elf_food in data_into_list:
        cals = sum([eval(i) for i in elf_food.split("\n")])
        max_cal_inventory.append(cals)
        if cals > most_calories:
            most_calories = cals

    max_cal_inventory.sort(reverse=True)

    # printing the data
    print(most_calories)
    print(sum(max_cal_inventory[0:3]))
