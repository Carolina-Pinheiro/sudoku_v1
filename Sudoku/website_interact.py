###Module Description###
#----------------------------------------------
# Function: interacts with the website 

###Modules###
import numpy 
import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys

##Variables##
difficulty = 2 #0->easy, 1-> medium, 2-> dificult, 3->expert


#----------------------------------------------
# Function: Initializes the browser, accepts the cookies, changes the difficulty
# Input: url -> url of the website in question (sudoku.com), browser -> driver for the browser that's being used
# Output: content of the website
def init(url, browser):
    browser.get(url)              #opens url given
    delay=10 #seconds
    print('Browser Opened')

    accepts_cookies(browser,delay)                      #acepts cookies
    difficulty_select(browser,delay,difficulty)                  #selects difficulty

    return (content(browser,delay))                     #returns website's content



#----------------------------------------------
# Function: Accepts the cookies pop-up that appears when the site is opened for the first time
# Input:  browser -> driver for the browser that's being used, delay-> wait time before quitting,
# Output: ---
def accepts_cookies(browser,delay):
    try:
        cookies = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#banner-accept')))  #waits for cookies banner to be presented
        print ("Cookies Located")
    except TimeoutException:
        print ("Loading took too much time, quitting...")
        browser.quit()
        sys.exit()

    cookies.click()                #accepts cookies
    print('Cookies Accepted')



#----------------------------------------------
# Function: Selects the difficulty
# Input: browser -> driver for the browser that's being used, delay-> wait time before quitting, dif-> difficulty (0->easy, 1-> medium, 2-> dificult, 3->expert)
# Output: ---
def difficulty_select(browser,delay,dif):
    try:
        menu = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "difficulty-label"))) #waits for difficulty menu to be available
        print ("Difficulty located")
    except TimeoutException:
        print ("Loading took too much time,quitting...")
        browser.quit()
        sys.exit()
    
    menu.click()                                            #opens difficulty menu
    expert = menu.find_elements_by_tag_name("li")[dif]      #finds the list of difficulties ("li" is the list tag)
    expert.click()                                          #selects expert difficulty



#----------------------------------------------
# Function: retrieves website's content with the help of BeautifulSoup module
# Input: browser-> driver for the browser that's being used
# Output: relevant content for the program, in this case only the information in the "div.cell-value"
def content(browser,delay):
    try:
        element = WebDriverWait(browser, delay).until( EC.presence_of_element_located((By.CSS_SELECTOR, "#game > table > tbody > tr:nth-child(2) > td:nth-child(9) > div.cell-value"))   )  #waits for a cell value to be presentd, so as not to try to retrieve the information before that
    except TimeoutException:
        print ("Loading took too much time, quitting....")
        browser.quit()
        sys.exit()

    html = browser.page_source                          #fetches the page's html source
    soup = BeautifulSoup(html, 'lxml')                  #converts it into a "soup"
    return( (soup.tbody).select('div.cell-value') )     #return the relevant information



#----------------------------------------------
# Function: fills the grid in the website
# Input: browser-> driver for the browser that's being used, grid-> solved grid (matrix) , original_grid-> unsolved grid (matrix)
# Output: ---
def input_grid(browser,grid,original_grid):
    for i in range (1,10,1):
        for j in range (1,10,1):
            if isEmpty(original_grid,i,j):              #if the cell is empty it interacts with it
                click_cell(i,j, browser,grid)           #clicks and fills the cell



#----------------------------------------------
# Function: checks if a cell was empty in the unsolved grid
# Input: original_grid -> unsolved grid (matrix), i,j-> positions to be analyzed
# Output: True if the cell is empty, False if it isn't
def isEmpty(original_grid,i,j):
    if original_grid[i-1][j-1]==0:  #cell is empty
        return  True
    else:
        return False



#----------------------------------------------
# Function: clicks and fills the cell
# Input: i->position of the cell given (from 1 to 9) line, j-> position of the cell given (from 1 to 9) column, browser->  driver for the browser that's being used, grid-> solved grid (matrix)
# Output: ---
def click_cell(i,j,browser,grid):
    cell = browser.find_element_by_css_selector('tr.game-row:nth-child(' +str(i)+') > td:nth-child('+str(j) +')')   #finds cell
    cell.click()                                                                                                    #clicks it
    cell=browser.find_element_by_css_selector('div.numpad-item:nth-child('+str(grid[i-1][j-1])+')')                 #finds number in numpad (there isn't a way to interact with the with the keyboard)
    cell.click()                                                                                                    #clicks it



