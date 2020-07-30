###Modules###
import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
import time

###Functions###
#----------------------------------------------
# Function: 
# Input: 
# Output: 
def input_grid(browser,grid,original_grid):
    for i in range (1,10,1):
        for j in range (1,10,1):
            if isEmpty(original_grid,i,j)==True:
                click_cell(i,j, browser,grid)


#----------------------------------------------
# Function: 
# Input: 
# Output: 
def click_cell(i,j,browser,grid):
    cell = browser.find_element_by_css_selector('tr.game-row:nth-child(' +str(i)+') > td:nth-child('+str(j) +')') 
    cell.click()
    cell=browser.find_element_by_css_selector('div.numpad-item:nth-child('+str(grid[i-1][j-1])+')')
    cell.click()

#----------------------------------------------
# Function: 
# Input: 
# Output: 
def isEmpty(original_grid,i,j):
    if original_grid[i-1][j-1]==0:
        return  True
    else:
        return False