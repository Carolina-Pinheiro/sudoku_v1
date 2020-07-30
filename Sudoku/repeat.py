import numpy 
import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
import time
import numpy

import complete
import solver
import info

#----------------------------------------------
# Function: 
# Input: 
# Output: 
def new_game_button(browser):
    delay=5
    try:
        ng = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, "    #sudoku-wrapper > div.game-flex-wrapper > div.game-wrapper > div.win-overlay > div.win-content-wrapper > div.button.button-play")))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
        browser.quit()

    ng.click()

#----------------------------------------------
# Function: 
# Input: 
# Output: 
def repeat_game(browser):
    new_game_button(browser) #clicks the new game button

    elements=info.content(browser,10)
    original_grid=info.fill_grid(elements) #retrieves grid info
    grid=original_grid.copy()

    print(numpy.matrix(original_grid))
    print('Solving the puzzle...')

    solver.solved_variable(False)
    grid=solver.solve(grid) #solves grid

    print(numpy.matrix(grid))


    complete.input_grid(browser,grid,original_grid)#fills the grid