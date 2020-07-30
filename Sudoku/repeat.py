###Module Description###
#----------------------------------------------
# Function: handles all the things after the first puzzle was solved



import numpy 
import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys

import website_interact
import solver
import data_processing

#----------------------------------------------
# Function: clicks the new game button
# Input: browser-> driver for the browser that's being used
# Output: 
def new_game_button(browser):
    delay=10
    try:
        ng = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#sudoku-wrapper > div.game-flex-wrapper > div.game-wrapper > div.win-overlay > div.win-content-wrapper > div.button.button-play")))  #waits for the new game button to be available
        print ("New game button located")
    except TimeoutException:
        print ("Loading took too much time, quitting....")
        browser.quit()
        sys.exit()

    ng.click()          #clicks the new game button


#----------------------------------------------
# Function: repeat_game loop, repeats all the game phases
# Input: browser-> driver for the browser that's being used
# Output: 
def repeat_game(browser):
    new_game_button(browser)                                    #clicks the new game button

    elements=website_interact.content(browser,10)                   
    original_grid=data_processing.fill_grid(elements)                      #retrieves grid info
    grid=original_grid.copy()                                   #saves a copy of the original grid

    print(numpy.matrix(original_grid))
    print('Solving the puzzle...')

    solver.solved_variable(False)                               #sets solved variable to False
    grid=solver.solve(grid)                                     #solves grid

    print(numpy.matrix(grid))


    website_interact.input_grid(browser,grid,original_grid)     #fills the grid



