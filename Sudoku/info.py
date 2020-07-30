###Module Description###
#----------------------------------------------
# Function: Deals with the website's info. Retrieve's the information present and prepares it to be used by other functions.

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


###Variables###
dim=[0,0]
svg=[
    [12,30], #1
    [20,31], #2
    [21,32], #3
    [24,30], #4
    [21,31], #5
    [22,32], #6
    [20,30], #7
    [22,32], #8
    [23,32], #9
    ]


###Functions###
#----------------------------------------------
# Function: Initializes the browser, accepts the cookies, changes the difficulty
# Input: url -> url of the website in question (sudoku.com), browser -> driver for the browser that's being used
# Output: content of the website
def init(url, browser):
    browser.get(url)              #opens url given
    delay=10 #seconds
    print('Browser Opened')

    try:
        cookies = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#banner-accept')))  #waits for cookies banner to be presented
        print ("Cookies Located")
    except TimeoutException:
        print ("Loading took too much time, quitting...")
        browser.quit()
        sys.exit()

    cookies.click()                #accepts cookies
    print('Cookies Accepted')

    try:
        menu = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "difficulty-label"))) #waits for difficulty menu to be available
        print ("Difficulty located")
    except TimeoutException:
        print ("Loading took too much time,quitting...")
        browser.quit()
        sys.exit()
    
    menu.click()                                        #opens difficulty menu
    expert = menu.find_elements_by_tag_name("li")[3]    #finds the list of difficulties ("li" is the list tag)
    expert.click()                                      #selects expert difficulty
    
    return (content(browser,delay))                     #returns website's content



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
# Function: copies the sudoku puzzle from the website to a matrix 
# Input: elements -> array, contains div.cell-value info, each position represents a cell
# Output: puzzle to be solved (in matrix form)
def fill_grid(elements):
    grid=numpy.zeros((9,9))                                     #blank grid, filled with zeros (0=cell to be filled)
    grid=grid.astype(int)                                       #the grid is created as a float, convert it to int
    for i in range (9):
        for j in range (9):       
            aux=elements[i*9+j].select('svg')                   #the numbers aren't hard-coded in the html, instead each number is defined by it's svg path, so we want to analyze this information 
            aux=str(aux)                                        #convert it to string to be easier to analyze, there were other ways to do this without converting it to a string, but for me this was the most intuitive
            if aux == '[]':                                     #if a cell is empty its svg value will be none
                grid[i][j] = 0
            else:
                height = aux.find('height')                     #the height and width (present in the svg) define a number
                width = aux.find('width')                       #height and width now have the positions within the string where these words start
            
                if height != -1 and width != -1:                #if the code doesn't find height or width it returns -1
                    dim[0]= int(aux[width+len('width="')] + aux[width+len('width="')+1])                #width and height are 2 digit numbers
                    dim[1]= int(aux[height+len('height="')] + aux[height+len('height="')+1])
                
                grid[i][j] = find_match(svg,dim,aux)            #to find which number is represented
    return grid             



#----------------------------------------------
# Function: by receiving the svg info, it finds which number it represents
# Input: svg -> list of arrays which contains the width and height of which number in svg, dim-> the svg being analyzed, aux-> the string which contains all the svg info
# Output: the number represented
def find_match(svg,dim,aux):
    for i in range(9):            
        if svg[i] == dim and ( (i+1) !=6 and (i+1)!=8):         #6 and 8 have the same height and width so we have to find another method
            return (i+1)
        elif svg[i]== dim:
            d = aux.find('d="')
            aux2=aux[ d+len('d="') : d+7+len('d="')]
            if aux2 == 'M10.964':                               #this parameter is one that distinguishs 6 from the 8, M10.964 for 6 and M10.533 for 8
                return 6
            else:
                return 8