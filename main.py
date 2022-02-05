board =[[0,0,0,0],[2,2,2,16],[4,4,4,4],[0,25,0,2]]
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
