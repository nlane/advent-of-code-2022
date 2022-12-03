from days import utils

shape_score = {
  "A": 1,
  "B": 2,
  "C": 3
}

x_to_a_map = {
  "X": "A",
  "Y": "B",
  "Z": "C"
}

convert_hands_win = {
  "A" : "B", # rock -> paper
  "B" : "C", # paper -> scissors
  "C" : "A"  # scissors -> rock
}

convert_hands_loss = {
  "A" : "C", # rock -> scissors
  "B" : "A", # paper -> rock
  "C" : "B"  # scissors -> paper
}


def win_score(opponent_hand, my_hand):
  # draw
  if opponent_hand == my_hand:
    return 3 + shape_score[my_hand]
  # rock beats scissors
  elif my_hand == "A" and opponent_hand == "C":
    return 6 + shape_score[my_hand]
  # paper beats rock
  elif my_hand == "B" and opponent_hand == "A":
    return 6 + shape_score[my_hand]
  # scissors beats paper
  elif my_hand == "C" and opponent_hand == "B":
    return 6 + shape_score[my_hand]
  # otherwise it's a loss
  else:
    return shape_score[my_hand]


def part1_score(game_results):
  opponent_hand = game_results[0]
  my_hand = x_to_a_map[game_results[2]]
  return win_score(opponent_hand, my_hand)

def part2_score(game_results):
  opponent_hand = game_results[0]
  my_strategy = game_results[2]
  # lose
  if my_strategy == "X":
    return win_score(opponent_hand, convert_hands_loss[opponent_hand])
  # win
  elif my_strategy == "Z":
    return win_score(opponent_hand, convert_hands_win[opponent_hand])
  # draw
  else:
    return win_score(opponent_hand, opponent_hand)


def main():
  games_str = utils.open_file(2)
  games = games_str.split("\n")
  total = 0
  total2 = 0
  for game in games:
    total += part1_score(game)
    total2 += part2_score(game)
  print(total)
  print(total2)