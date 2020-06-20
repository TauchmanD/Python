def printSudoku(sudoku):
    for x in range(9):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - -")
        print("{} {} {} | {} {} {} | {} {} {}".format(sudoku[x][0], sudoku[x][1], sudoku[x][2], sudoku[x][3], sudoku[x][4], sudoku[x][5], sudoku[x][6], sudoku[x][7], sudoku[x][8]))
    print("\n Sudoku Printed!\n")

def findEmpty(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                return (x, y)
            else:
                return False

def isValid(sudoku, number, place):
    # row
    for i in range(9):
        if sudoku[place[0]][i] == number and place[1] != i:
            return False

    # column
    for i in range(9):
        if sudoku[i][place[1]] == number and place[0] != i:
            return False

    #box
    boxX = place[0] // 3
    boxY = place[1] // 3
    for x in range(boxX*3, boxX*2+3):
        for y in range(boxY*3, boxY*2+3):
            if sudoku[x][y] == number and (x, y) != place:
                return False
    return True
def solve(sudoku):
    place = findEmpty(sudoku)
    printSudoku(sudoku)
    if not place:
        return True
    else:
        row, column = place
    for i in range(1, 10):
        if isValid(sudoku, i, (row, column)):
            sudoku[row][column] = i
            if solve(sudoku):
                return True
            sudoku[row][column] = 0
    return False


sudoku = [
    [1, 0, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3]
]
printSudoku(sudoku)
solve(sudoku)
printSudoku(sudoku)
