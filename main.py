board =[[0,0,0,0],[2,2,2,2],[4,4,4,4],[0,2,0,2]]
boardsize = 4
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
        currentboard[i] = reverse(currentboard[i])
    return currentboard
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
display()
merge_left(board)
display()
merge_right(board)
display()