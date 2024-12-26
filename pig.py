import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)
    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4 players.")
    else:
        print("Invalid, Try Again")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer Number", player_idx + 1, "turn has just started!\n")
        print("Your Current Scores:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll? (y): ")
            if should_roll.lower() != "y":
                break

            roll_val = roll()
            if roll_val == 1:
                print("You rolled a 1! Turn Done!")
                current_score = 0
                break
            else:
                current_score += roll_val
                print("You rolled a:", roll_val)

            print("Your current score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your current score is:", player_scores[player_idx])

max_score = max(player_scores)
winners = [idx + 1 for idx, score in enumerate(player_scores) if score == max_score]
if len(winners) > 1:
    print("It's a tie! Players", ', '.join(map(str, winners)), "win with a score of:", max_score)
else:
    print("Player number", winners[0], "wins with a score of:", max_score)