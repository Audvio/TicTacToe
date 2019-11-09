import time

print("Choose your mark and type digit matching to place on board.")

board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
occupied_spaces = []
user_spaces = []
computer_spaces = []
opponent_mark = []
user_mark = []


def draw_board():
    print(board[0], '|', board[1], '|', board[2])
    print('---------')
    print(board[3], '|', board[4], '|', board[5])
    print('---------')
    print(board[6], '|', board[7], '|', board[8])


from random import randint, random


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


def user_move():
    place_mark = int
    while place_mark not in board:
        place_mark = int(input("Where do you want to place your mark?: "))
        if place_mark in range(len(board)) and place_mark not in occupied_spaces:
            board[place_mark] = user_mark
            occupied_spaces.append(place_mark)
            user_spaces.append(place_mark)
            break
        else:
            print("Incorrect mark was chosen or place is taken")


def computer_move():
    choose = int
    while choose not in board:
        choose = randint(0, 8)
        if choose not in occupied_spaces:
            board[choose] = opponent_mark[0]
            occupied_spaces.append(choose)
            computer_spaces.append(choose)
            break


def winner():
    winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for list in winning_combinations:

        if all(el in user_spaces for el in list):
            print("You have won! :D")
            exit()
        elif all(el in computer_spaces for el in list):
            print("You have loose. :/")
            exit()


def if_tie():
    if len(occupied_spaces) == 9:
        print("TIE!")
        exit()


def random_order():
    result = randint(0, 1)
    print("I draw the order")
    time.sleep(0.7)
    for i in range(5):
        print('.', end='..', flush=True)
        time.sleep(0.4)
    return result
