from functions import draw_board, opponent_mark, user_mark, user_move, computer_move, winner, if_tie, random_order

draw_board()

while user_mark == []:
    choose_mark = input('Circle or cross?(O/X): ')
    if choose_mark == 'O' or choose_mark == 'o':
        opponent_mark.append("X")
        user_mark = 'O'
        print('You have chosen circle ')
        break
    elif choose_mark == 'X' or choose_mark == 'x':
        opponent_mark.append("O")
        user_mark = 'X'
        print('You have chosen cross')
        break
    else:
        print("Choose correct sign!")

result = random_order()
if result == 1:
    print("You start.")
    while True:
        user_move()
        winner()
        if_tie()
        computer_move()
        draw_board()
        winner()
        if_tie()
else:
    print("Computer starts.")
    while True:
        computer_move()
        draw_board()
        winner()
        if_tie()
        user_move()
        winner()
        if_tie()


