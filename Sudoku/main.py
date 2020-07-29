###Modules###
import numpy 
from selenium import webdriver

import solver
import info
import complete
###Variables###

grid=numpy.zeros((9,9))
grid=grid.astype(int)

url="https://sudoku.com/pt"

browser = webdriver.Chrome(executable_path=r'C:\Users\cppin\Desktop\Python\chromedriver.exe')


###Main##

elements=info.init(url, browser) #opens browser and prepares game
grid=info.fill_grid(elements) #retrieves grid info
print(numpy.matrix(grid))
print('Solving the puzzle...')
grid=solver.solve(grid) #solves grid
print(numpy.matrix(grid))
complete.fill_grid(browser,grid)#fills the grid
