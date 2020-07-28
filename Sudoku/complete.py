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
def click_cell(i,j,browser,grid):
    cell = browser.find_element_by_css_selector('tr.game-row:nth-child(' +str(i)+') > td:nth-child('+str(j) +')') 
    cell.click()
    cell=browser.find_element_by_css_selector('div.numpad-item:nth-child('+str(grid[i-1][j-1])+')')
    cell.click()
