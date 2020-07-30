
###Variables###
solved = False


###Functions###
#----------------------------------------------
# Function: 
# Input: 
# Output: 
def possible (lin,col,n, grid):
    for i in range(9):
        if grid[lin][i] == n: #check line
            #print ("line")
            return False
        elif grid[i][col] == n: #check col
            #print ("col")
            return False
    x=int(col/3)
    y=int(lin/3)

    for k in range(3*x,3*x+3,1):
        for j in range(3*y, 3*y+3,1):
            if grid[j][k]== n:
                return False
        j=3*y
    return True



#----------------------------------------------
# Function: 
# Input: 
# Output: 
def solve(grid):
    global solved
    for i in range (9):
        #print("Line", i)
        for j in range (9):
            #print("Col",j)
            if grid[i][j] == 0: #cell is empty
                for n in range (1,10,1): #check all numbers
                    if possible(i,j,n,grid):
                        grid [i][j] = n
                        #print(i,j,n)
                        grid=solve(grid)
                        if solved == False:
                            grid [i][j] =0
                return grid
    solved = True
    return grid

#----------------------------------------------
# Function: 
# Input: 
# Output: 
def solved_variable(value):
    global solved
    solved = value
