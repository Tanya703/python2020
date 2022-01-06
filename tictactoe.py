#tictactoe team project
import random
L = [[" ", "A", "B", "C"],["1", " ", " ", " "],["2", " ", " ", " "],["3", " ", " ", " "]]

def grid():
    for row in L:
        for cell in row:
            print(cell, end=" ")
        print()

def play(c, r):
    if c=="A":
        if r=="1":
            L[1][1]="X"
        elif r=="2":
            L[2][1]="X"
        elif r=="3":
            L[3][1]="X"
    elif c =="B":
        if r=="1":
            L[1][2]="X"
        elif r=="2":
            L[2][2]="X"
        elif r=="3":
            L[3][2]="X"
    elif c =="C":
        if r=="1":
            L[1][3]="X"
        elif r=="2":
            L[2][3]="X"
        elif r=="3":
            L[3][3]="X"

def computer_play():
    taken = True
    while taken:
        col= random.randint(1,3)
        row = random.randint(1,3)
        if L[col][row] == " ":
            L[col][row] = "O"
            taken = False

def check_cell(c, r):
    if c=="A":
        if r=="1":
            if L[1][1]==" ":
                return True
        elif r=="2":
            if L[2][1] == " ":
                return True
        elif r=="3":
            if L[3][1] == " ":
                return True
    elif c =="B":
        if r=="1":
            if L[1][2] == " ":
                return True
        elif r=="2":
            if L[2][2] == " ":
                return True
        elif r=="3":
            if L[3][2]  == " ":
                return True
    elif c =="C":
        if r=="1":
            if L[1][3] == " ":
                return True
        elif r=="2":
            if L[2][3] == " ":
                return True
        elif r=="3":
            if L[3][3] == " ":
                return True
        else:
            return False
    
def check_win():
    #win = False
    for row in L:
        for i in range(1,4):
            if [str(i),"X","X","X"] == row:
                return "human", True
            if [str(i),"O","O","O"] == row:
                return "computer", True
    for j in range(1,4):
        if L[1][j] == L[2][j] and L[3][j] == L[1][j] and L[2][j] == L[3][j]:
            if L[1][j] == "X":
                return "human", True
            if L[1][j] == "O":
                return "computer", True
    if L[1][1] == L[2][2] and L[1][1] == L[3][3]:
            if L[1][1] == "X":
                return "human", True
            if L[1][1] == "O":
                return "computer", True
    if L[1][3] == L[2][2] and L[1][1] == L[3][1]:
            if L[3][1] == "X":
                return "human", True
            if L[3][1] == "O":
                return "computer", True
    return "", False
    
def main():
    play_count = 0
    win = False
    next_turn, who = "", ""

    if random.randint(0,9) > 4:
        c, r = input("You start! Give a cell (col,row): ").split()
        play(c, r)
        next_turn = "c"
    else:
        print("Computer starts! ")
        computer_play()
        next_turn = "h"
        
    play_count += 1
    grid()

    while play_count < 9 and not win:
        if next_turn == "c":
            computer_play()
            print("Computer has played")
            next_turn = "h"
            play_count += 1
        else:
            c, r = input("Give a cell (col,row): ").split()
            if check_cell(c.upper(),r):
                play(c, r)
                next_turn = "c"
                play_count += 1
            else:
                print("Cell is taken!")
        grid()
        who, win = check_win()
        if win:
            if who == "computer":
                print("You lose!")
            elif who == "human":
                print("You win!")
    if play_count == 9 and not win:
        print("It's a draw!")
                
main()
