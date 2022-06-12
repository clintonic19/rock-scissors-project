import random
import math


def play():
    user = input(
        "What's your choice? 'R' for rock, 'P' for paper, 'S' for scissors\n")
    user = user.lower()

    computer = random.choice(['R', 'P', 'S'])
    computer = computer.lower()

    if user == computer:
        return (0, user, computer)

    # r > s, s > p, p > r
    if winner(user, computer):
        return (1, user, computer)

    return (-1, user, computer)


def winner(player, opponent):
    # return true is the player beats the opponent
    # winning conditions: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False


def play_best(number_of_wins):
    # play against the computer until someone wins best of n games
    # to win, you must win ceil(n/2) games (ie 2/3, 3/5, 4/7)
    player_wins = 0
    computer_wins = 0
    possible_wins = math.ceil(number_of_wins/2)

    while player_wins < possible_wins and computer_wins < possible_wins:
        result, user, computer = play()
        # tie
        if result == 0:
            print(
                'It is a tie. You and the computer have both chosen {}. \n'.format(user))
        # you win
        elif result == 1:
            player_wins += 1
            print('You chose {} and the computer chose {}. You won!\n'.format(
                user, computer))
        else:
            computer_wins += 1
            print(
                'You chose {} and the computer chose {}. You lost :(\n'.format(user, computer))

    if player_wins > computer_wins:
        print("You have won the best of {} games! you're a champ: ".format(
            number_of_wins))
    else:
        print('The computer has won the best of {} games. try harder next time!'.format(
            number_of_wins))


if __name__ == '__main__':
    play_best(3)  # 2
