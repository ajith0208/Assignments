# 3. Create a basic rock paper scissors game.
# Take 2 user inputs from 2 players. You can use R, P and S are possible user inputs. Play the game
# for 10 rounds and declare the winner.
# Rules of the game
# Rock vs Scissors - Rock wins
# Rock vs Paper - Paper wins
# Paper vs Scissors - Scissor wins
# Eg: Game 1: Player1 = R, Player2 = S, Output: Player1 wins
# Player1 = P, Player2 = P, Output: Draw
# Final Winner: Player with maximum wins
player1 = 0
player2 = 0
round = 1
while True:
    print(f'____ Round - {round} ____')
    p1 = input('Player1 : Enter your choice (R, P, S) : ').lower()
    p2 = input('Player2 : Enter your choice (R, P, S) : ').lower()

    if p1 == p2:
        print('Output : Draw')
    elif p2 not in ['r', 'p', 's']:
        round -= 1
        print('Invalid input')
    elif p1 == 'r':
        if p2 == 's':
            print('Output : Player1 wins')
            player1 += 1
        else:
            print('Output : Player2 wins')
            player2 += 1
    elif p1 == 'p':
        if p2 == 's':
            print('Output : Player2 wins')
            player2 += 1
        else:
            print('Output : Player1 wins')
            player1 += 1
    elif p1 == 's':
        if p2 == 'p':
            print('Output : Player1 wins')
            player1 += 1
        else:
            print('Output : Player2 wins')
            player2 += 1
    else:
        print('Invalid input')
        round -= 1

    round += 1
    print(f'Score - Player1 = {player1} & Player2 = {player2}')
    print('______________________________________________')
    if round == 11:
        print(f'___ Final Score ___ \nPlayer1 = {player1} \nPlayer2 = {player2}\n')
        if player1 == player2:
            print('** Draw **')
        elif player1 > player2:
            print('** Player1 Wins **')
        else:
            print('** Player2 Wins **')
        print('\n___ Game Completed ___')
        break
