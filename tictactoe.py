import time
import os

board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]
player = ""

def print_board():
    print("  " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("-------------")
    print("  " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("-------------")
    print("  " + board[7] + " | " + board[8] + " | " + board[9] + " ")

def is_winner(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
        (board[4] == player and board[5] == player and board[6] == player) or \
        (board[7] == player and board[8] == player and board[9] == player) or \
        (board[1] == player and board[4] == player and board[7] == player) or \
        (board[2] == player and board[5] == player and board[8] == player) or \
        (board[3] == player and board[6] == player and board[9] == player) or \
        (board[1] == player and board[5] == player and board[9] == player) or \
        (board[3] == player and board[5] == player and board[7] == player):
        
        return True
    else:
        return False

def is_board_full(board):
    if " " in board:
        return False
    else:
        return True

while True:
    #Player X
    os.system("cls")
    print_board()
    choice = 0
    
    while choice not in (1, 2, 3, 4, 5 , 6, 7, 8, 9):
        choice = int(input("Please take between 1 - 9:\n"))

    if board[choice] == " ":
        board[choice] = "X"
    else:
        print("Invalid sign")
        time.sleep(1)

    if is_winner(board, "X"):
        print("X wins! Congratulations")
        print_board()
        time.sleep(3)
        os.system("cls")

    if is_board_full(board):
        os.system("cls")
        print_board()
        print("Tie!")
        time.sleep(1)
        break

    #Player O
    os.system("cls")
    print_board()
    choice = 0
    
    while choice not in (1, 2, 3, 4, 5 , 6, 7, 8, 9):
        choice = int(input("Please take between 1 - 9:\n"))

    if board[choice] == " ":
        board[choice] = "O"
    else:
        print("Invalid sign")
        time.sleep(1)

    if is_winner(board, "O"):
        print("O wins! Congratulations")
        print_board()
        time.sleep(3)
        os.system("cls")

    if is_board_full(board):
        os.system("cls")
        print_board()
        print("Tie!")
        time.sleep(1)
        break