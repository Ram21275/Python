def ifPossible(x,y,n): 
    #checks the rows
    for i in range(0,9):
        if sudoku[i][x] == n and i != y:
            return False
        
    #checks the columns
    for i in range(0,9):
        if sudoku[y][i] == n and i != x:
            return False
        
    #checks the boxes
    xx = 3 * (x // 3)
    yy = 3 * (y // 3)

    for i in range(xx,xx+3):
        for j in range(yy, yy+3):
            if sudoku[j][i] == n:
                return False
        
    return True

def solveSudoku():
    global sudoku
    #solving the sudoku
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for n in range(1,10):
                    if ifPossible(x,y,n):
                        sudoku[y][x] = n
                        solveSudoku()
                        sudoku[y][x] = 0 #Backtracking
                return
    for i in sudoku:
        print(i)

sudoku = [  
            [3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0], 
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]
        ]  

solveSudoku()
