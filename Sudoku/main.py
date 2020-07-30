###Modules###
import numpy 
from selenium import webdriver

import solver
import info
import complete
###Variables###

original_grid=numpy.zeros((9,9))
original_grid=original_grid.astype(int)
grid=numpy.zeros((9,9))
grid=grid.astype(int)

url="https://sudoku.com/pt"

browser = webdriver.Chrome(executable_path=r'C:\Users\cppin\Desktop\Python\chromedriver.exe')


###Main##

elements=info.init(url, browser) #opens browser and prepares game
original_grid=info.fill_grid(elements) #retrieves grid info
grid=original_grid.copy()

print(numpy.matrix(original_grid))
print('Solving the puzzle...')

grid=solver.solve(grid) #solves grid

print(numpy.matrix(grid))


complete.input_grid(browser,grid,original_grid)#fills the grid
