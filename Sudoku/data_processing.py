###Module Description###
#----------------------------------------------
# Function: Processes the data 

###Modules###
import numpy 
import bs4
from bs4 import BeautifulSoup

###Variables###
dim=[0,0]
svg=[
    [12,30], #1
    [20,31], #2
    [21,32], #3
    [24,30], #4
    [21,31], #5
    [22,32], #6
    [20,30], #7
    [22,32], #8
    [23,32], #9
    ]


###Functions###
#----------------------------------------------
# Function: copies the sudoku puzzle from the website to a matrix 
# Input: elements -> array, contains div.cell-value info, each position represents a cell
# Output: puzzle to be solved (in matrix form)
def fill_grid(elements):
    original_grid=numpy.zeros((9,9))                                     #blank grid, filled with zeros (0=cell to be filled)
    original_grid=original_grid.astype(int)                              #the grid is created as a float, convert it to int
    for i in range (9):
        for j in range (9):       
            grid=read_cell(elements,i,j,original_grid)
    return original_grid             


#----------------------------------------------
# Function: reads each cell
# Input: elements-> array, contains div.cell-value info, each position represents a cell , i,j -> grid position, original_grid-> unsolved grid (matrix)
# Output: original_grid -> unsolved gird (matrix)
def read_cell(elements,i,j,original_grid):
    svg_cell=elements[i*9+j].select('svg')                      #the numbers aren't hard-coded in the html, instead each number is defined by it's svg path, so we want to analyze this information 
    svg_cell=str(svg_cell)                                      #convert it to string to be easier to analyze, there were other ways to do this without converting it to a string, but for me this was the most intuitive
    if svg_cell == '[]':                                        #if a cell is empty its svg value will be none
        original_grid[i][j] = 0
    else:
        height =svg_cell.find('height')                         #the height and width (present in the svg) define a number
        width = svg_cell.find('width')                          #height and width now have the positions within the string where these words start
    
        if height != -1 and width != -1:                        #if the code doesn't find height or width it returns -1
            dim[0]= int(svg_cell[width+len('width="')] + svg_cell[width+len('width="')+1])                #width and height are 2 digit numbers
            dim[1]= int(svg_cell[height+len('height="')] +svg_cell[height+len('height="')+1])
        
        original_grid[i][j] = find_match(svg,dim,svg_cell)            #to find which number is represented
    return original_grid


#----------------------------------------------
# Function: by receiving the svg info, it finds which number it represents
# Input: svg -> list of arrays which contains the width and height of which number in svg, dim-> the svg being analyzed, aux-> the string which contains all the svg info
# Output: the number represented
def find_match(svg,dim,svg_cell):
    for i in range(9):            
        if svg[i] == dim and ( (i+1) !=6 and (i+1)!=8):         #6 and 8 have the same height and width so we have to find another method
            return (i+1)
        elif svg[i]== dim:
            d = svg_cell.find('d="')
            svg_cell_d=svg_cell[ d+len('d="') : d+7+len('d="')]
            if svg_cell_d == 'M10.964':                               #this parameter is one that distinguishs 6 from the 8, M10.964 for 6 and M10.533 for 8
                return 6
            else:
                return 8