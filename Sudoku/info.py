###Modules###
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
# Function: 
# Input: 
# Output: 
def init(url, browser):
    browser.get(url)
    delay=10 #seconds
    print('Browser Opened')

    try:
        cookies = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#banner-accept')))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
        browser.quit()

    cookies.click()
    print('Cookies Accepted')

    try:
        menu = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "difficulty-label")))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")
        browser.quit()
    
    menu.click()
    print("Vou tentar")
    expert = menu.find_elements_by_tag_name("li")[3] #finds the list ("li" is the list tag)
    expert.click()

    print('Expert')
    
    try:
        element = WebDriverWait(browser, delay).until( EC.presence_of_element_located((By.CSS_SELECTOR, "#game > table > tbody > tr:nth-child(2) > td:nth-child(9) > div.cell-value"))   )
    except TimeoutException:
        print ("Loading took too much time!")
        browser.quit()

    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    return( (soup.tbody).select('div.cell-value') )



#----------------------------------------------
# Function: 
# Input: 
# Output: 
def find_match(svg,dim,aux):
    for i in range(9):
        if svg[i] == dim and ( (i+1) !=6 and (i+1)!=8):
            return (i+1)
        elif svg[i]== dim:
            d = aux.find('d="')
            aux2=aux[ d+len('d="') : d+7+len('d="')]
            if aux2 == 'M10.964':
                return 6
            else:
                return 8


#----------------------------------------------
# Function: 
# Input: 
# Output: 
def fill_grid(elements):
    grid=numpy.zeros((9,9))
    grid=grid.astype(int)
    for i in range (9):
        for j in range (9):       
            aux=elements[i*9+j].select('svg')
            aux=str(aux)
            if aux == '[]': #comparar com o comprimento
                grid[i][j] = 0
            else:
                height = aux.find('height')
                width = aux.find('width')
            
                if height != -1 and width != -1:
                    dim[0]= int(aux[width+len('width="')] + aux[width+len('width="')+1])
                    dim[1]= int(aux[height+len('height="')] + aux[height+len('height="')+1])
                
                grid[i][j] = find_match(svg,dim,aux)
    return grid



