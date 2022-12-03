from days import utils

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority = {}
for i in range(len(letters)):
  letter = letters[i]
  priority[letter] = i + 1

def main():
  input_str = utils.open_file(3)
  rucksacks = input_str.split("\n")
  total = 0
  for sack in rucksacks:
    compartment1 = sack[0:len(sack)//2]
    compartment2 = sack[len(sack)//2:]
    common_item, = set([*compartment1]).intersection(set([*compartment2]))
    total += priority[common_item]
  print(total)

  total2 = 0
  for i in range(0, len(rucksacks), 3):
    badge, = set([*rucksacks[i]]).intersection([*rucksacks[i+1]],[*rucksacks[i+2]])
    total2 += priority[badge]
  print(total2)

