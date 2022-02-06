import copy 
import random

boardsize = 4
def display():
    largest = board[0][0]
    for row in board:
        for num in row:
            if num > largest:
                largest = num
    numspaces = len(str(largest))
    for row in board:
        output = "|"
        for num in row:
            if num == 0:
                output += " " * numspaces + "|"
            else:
                output += (" " * (numspaces - len(str(num)))) + str(num) + "|"
        print(output)
    print()

def mergeonerowleft(row):
    for j in range(boardsize -1):
        for i in range(boardsize -1, 0, -1):
            if row[i-1] == 0:
               row[i-1] = row[i]
               row[i] = 0
    for i in range(boardsize -1):
        if row[i] == row[i+1]:
            row[i] *=2
            row[i+1] = 0
    for i in range(boardsize -1, 0, -1):
        if row[i-1] == 0:
            row[i-1] = row[i]
            row[i] = 0
    return row

def merge_left(currentboard):
    for i in range(boardsize):
        currentboard[i] = mergeonerowleft(currentboard[i])
    return currentboard

def reverse(row):
    new=[]
    for i in range(boardsize -1,-1,-1):
        new.append(row[i])
    return new

def merge_right(currentboard):
    for i in range(boardsize):
        currentboard[i] = reverse(currentboard[i])
        currentboard[i] = mergeonerowleft(currentboard[i])
        currentboard[i] = reverse(currentboard[i]
        )
    return currentboard

def transpose(currentboard):
    for j in range(boardsize):
        for i in range(j, boardsize):
            if not i == j:
                temp = currentboard[j][i]
                currentboard[j][i] = currentboard[i][j]
                currentboard[i][j] = temp
    return currentboard

def merge_up(currentboard):
    currentboard = transpose(currentboard)
    currentboard = merge_left(currentboard)
    currentboard = transpose(currentboard)
    return currentboard

def merge_down(currentboard):
    currentboard = transpose(currentboard)
    currentboard = merge_right(currentboard)
    currentboard = transpose(currentboard)
    return currentboard

def chooseavalue():
     if random.randint(1,8) == 1:
        return 4
     else:
        return 2

def addnewvalue():
    rownum = random.randint(0, boardsize - 1)
    colnum = random.randint(0, boardsize - 1)

    while not board[rownum][colnum] == 0:
        rownum = random.randint(0, boardsize - 1)
        colnum = random.randint(0, boardsize - 1)
    
    board[rownum][colnum] = chooseavalue()


    
board = []
for i in range(boardsize):
    row = []
    for j in range(boardsize):
       row.append(0)
    board.append(row)

numwanted = 2
while numwanted > 0:
   rownum = random.randint(0, boardsize - 1)
   colnum = random.randint(0, boardsize - 1)

   if board[rownum][colnum] == 0:
       board[rownum][colnum] = chooseavalue()
       numwanted -= 1

print("HAI!! Welcome to 2048 your goal is to combine values to get the number 2048,by merging the board in differnet directions.Each and every time you will need to type'1' to merge left ,'2' to merge right,'3' to merge up, and '4' to merge down.\n Here is the starting board: ")
display()

gameover = False

while not gameover:
    move=input("which way do you want to merge")
    
    validinput = True
    tempboard = copy.deepcopy(board)

    if move == "1":
        board = merge_left(board)
    elif move == "2":
        board = merge_right(board)
    elif move == "3":
        board = merge_up(board)
    elif move == "4":
        board = merge_down(board)
    else:
        validinput = False

    if not validinput:
        print("your input was not valid,please try again by entering a valid input")
    else:
        if board == tempboard:
            print("try a different direction!!!")
        else:
            addnewvalue()
            display()
