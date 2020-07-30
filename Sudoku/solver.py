###Module Description###
#----------------------------------------------
# Function: Backtracking algorithm that solves the sudoku puzzle given 


###Variables###
solved = False


###Functions###
#----------------------------------------------
# Function: determines if a given cell can contain a number, taking into account the restritions of a sudoku puzzle
# Input: lin-> line of the cell given, col-> column of the cell given, n->number that we are trying to put in the cell, grid-> matrix that contains the puzzle
# Output: returns True if the number n can be in that cell, False if it can't
def possible (lin,col,n, grid):
    for i in range(9):
        if grid[lin][i] == n:           #check line
            return False
        elif grid[i][col] == n:         #check col
            return False
    
    x=int(col/3)                        #determines which subgrid the cell is located
    y=int(lin/3)

    for k in range(3*x,3*x+3,1):
        for j in range(3*y, 3*y+3,1):
            if grid[j][k]== n:          #checks the subgrid
                return False
        j=3*y
    return True                         #if doens't break any restrition it the number n can be in that cell



#----------------------------------------------
# Function: recursive functions that solves the puzzle
# Input:  grid -> matrix with the state of the grid during the algorithm 
# Output: grid -> matrix with the state of the grid during the algorithm
def solve(grid):
    global solved
    for i in range (9):
        for j in range (9):
            if grid[i][j] == 0:                 #cell is empty
                for n in range (1,10,1):        #check all numbers
                    if possible(i,j,n,grid):    #if possible() is True
                        grid [i][j] = n         #puts number in the grid
                        grid=solve(grid)        #recursive function
                        if solved == False:     #once the puzzle is solved we don't want to change the grid again
                            grid [i][j] =0
                return grid
    solved = True
    return grid

#----------------------------------------------
# Function: sets the solved variable to a determined value
# Input: value -> True/False
# Output: 
def solved_variable(value):
    global solved
    solved = value
