board =[[0,0,0,0],[2,2,2,2],[4,4,4,4],[0,4,0,2]]
def display():
    for row in board:
        output = "|"
        for num in row:
            if num == 0:
                output += " |"
            else:
                output += str(num) + "|"
        print(output)
    print()
display()
