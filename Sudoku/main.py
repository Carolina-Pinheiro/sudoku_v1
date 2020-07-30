####--------------------Automatic Sudoku Solver for sudoku.com--------------------###
#Carolina Pinheiro, 
#carolina.p.pinheiro@tecnico.ulisboa.pt 
#Julho 2020

###Modules###
import numpy 
from selenium import webdriver

import solver
import info
import complete
import repeat


###Variables###
url="https://sudoku.com/pt"
browser = webdriver.Chrome(executable_path=r'C:\Users\cppin\Desktop\Python\chromedriver.exe') #chromedriver.exe needs to be present and the path changed accordingly
new_game=True


###Main##
solver.solved_variable(False)

elements=info.init(url, browser)                #opens browser and prepares game
original_grid=info.fill_grid(elements)          #retrieves grid info

grid=original_grid.copy()                       #saves a copy of the original grid

print(numpy.matrix(original_grid))              #prints the retrieved grid
print('Solving the puzzle...')                  #in expert level, some puzzle can take several seconds to solve

grid=solver.solve(grid)                         #solves puzzle with backtracking algorithm

print(numpy.matrix(grid))                       #prints the solved grid

complete.input_grid(browser,grid,original_grid) #fills the grid


while new_game==True:                           #new game cycle
    print('New game?Y/N')
    answer=input()                              #waits for user's answer

    if answer=='Y':
        repeat.repeat_game(browser)             #repeats game cycle (similiar to the one above)
    elif answer=='N':
        print('Bye!')
        browser.quit()                          #closes browser
        new_game=False                          #leaves cycle
    else:
        print('Invalid answer')                 #to ask for new input