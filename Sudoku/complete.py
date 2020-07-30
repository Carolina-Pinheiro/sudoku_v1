###Module Description###
#----------------------------------------------
# Function: interacts with the website in order to complete the puzzle 

###Modules###
import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
import time

###Functions###
#----------------------------------------------
# Function: fills the grid in the website
# Input: browser-> driver for the browser that's being used, grid-> solved grid (matrix) , original_grid-> unsolved grid (matrix)
# Output: 
def input_grid(browser,grid,original_grid):
    for i in range (1,10,1):
        for j in range (1,10,1):
            if isEmpty(original_grid,i,j):              #if the cell is empty it interacts with it
                click_cell(i,j, browser,grid)           #clicks and fills the cell


#----------------------------------------------
# Function: clicks and fills the cell
# Input: i->position of the cell given (from 1 to 9) line, j-> position of the cell given (from 1 to 9) column, browser->  driver for the browser that's being used, grid-> solved grid (matrix)
# Output: 
def click_cell(i,j,browser,grid):
    cell = browser.find_element_by_css_selector('tr.game-row:nth-child(' +str(i)+') > td:nth-child('+str(j) +')')   #finds cell
    cell.click()                                                                                                    #clicks it
    cell=browser.find_element_by_css_selector('div.numpad-item:nth-child('+str(grid[i-1][j-1])+')')                 #finds number in numpad (there isn't a way to interact with the with the keyboard)
    cell.click()                                                                                                    #clicks it

#----------------------------------------------
# Function: checks if a cell was empty in the unsolved grid
# Input: original_grid -> unsolved grid (matrix), i,j-> positions to be analyzed
# Output: True if the cell is empty, False if it isn't
def isEmpty(original_grid,i,j):
    if original_grid[i-1][j-1]==0:  #cell is empty
        return  True
    else:
        return False