###Modules###
import numpy 
from selenium import webdriver

import solver
import info
import complete
import repeat
###Variables###

original_grid=numpy.zeros((9,9))
original_grid=original_grid.astype(int)
grid=numpy.zeros((9,9))
grid=grid.astype(int)

url="https://sudoku.com/pt"

browser = webdriver.Chrome(executable_path=r'C:\Users\cppin\Desktop\Python\chromedriver.exe')


###Main##
solver.solved_variable(False)
elements=info.init(url, browser) #opens browser and prepares game
original_grid=info.fill_grid(elements) #retrieves grid info
grid=original_grid.copy()

print(numpy.matrix(original_grid))
print('Solving the puzzle...')

grid=solver.solve(grid) #solves grid

print(numpy.matrix(grid))


complete.input_grid(browser,grid,original_grid)#fills the grid

new_game=True
while new_game==True:
    print('New game?Y/N')
    answer=input()
    if answer=='Y':
        repeat.repeat_game(browser)
    elif answer=='N':
        print('Bye!')
        browser.quit()
        new_game=False
    else:
        print('Invalid answer')