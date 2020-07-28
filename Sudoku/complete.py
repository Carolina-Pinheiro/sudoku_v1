###Modules###
import bs4
from bs4 import BeautifulSoup
from selenium import webdriver

###Functions###
#----------------------------------------------
# Function: 
# Input: 
# Output: 
def click_cell(i,j,browser):
    cell = browser.find_element_by_css_selector('tr.game-row:nth-child(' +str(i)+') > td:nth-child('+str(j) +')') 
    cell.click()
    #cell = browser.find_element_by_css_selector('.cell-selected > div:nth-child(1)')
    #cell.send_keys('1')
