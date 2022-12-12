from days import utils


def main():
    turns = utils.open_file(11).split("\n\n")
    monkeys = [[] for _ in range(len(turns))]
    monkey_count = [0 for x in range(len(turns))]
    # initialize monkeys
    for i in range(len(turns)):
        starting_str = turns[i].split("\n")[1]
        monkeys[i] += [int(x) for x in starting_str.replace(",", "")[18:].split(" ")]
    # 20 rounds
    for i in range(20):
        for j in range(len(turns)):
            split_turn = turns[j].split("\n")
            while len(monkeys[j]):
                # for item in monkeys[j]:
                item = monkeys[j].pop(0)
                monkey_count[j] += 1
                # inspection
                op, val = split_turn[2].split("old ")[1].split(" ")
                if val == "old":
                    val = item
                if op == "*":
                    item *= int(val)
                else:
                    item += int(val)
                # relief (divide by 3)
                item = item // 3
                # test
                test = split_turn[3].split(" ")[-1]
                # consequences
                if item % int(test) == 0:
                    new_monkey = int(split_turn[4].split(" ")[-1])
                else:
                    new_monkey = int(split_turn[5].split(" ")[-1])
                monkeys[new_monkey].append(item)
    monkey_count.sort()
    print(monkey_count[-1] * monkey_count[-2])
