import numpy 
import bs4
from bs4 import BeautifulSoup
import requests
import webbrowser as wb
from selenium import webdriver
def possible (lin,col,n):
    for i in range(9):
        if grid[lin][i] == n: #check line
            #print ("line")
            return False
        elif grid[i][col] == n: #check col
            #print ("col")
            return False
    x=int(col/3)
    y=int(lin/3)

    for k in range(3*x,3*x+3,1):
        for j in range(3*y, 3*y+3,1):
            if grid[j][k]== n:
                return False
        j=3*y
    return True

def solve():
    global solved
    for i in range (9):
        #print("Line", i)
        for j in range (9):
            #print("Col",j)
            if grid[i][j] == 0: #cell is empty
                for n in range (1,10,1): #check all numbers
                    if possible(i,j,n):
                        grid [i][j] = n
                        #print(i,j,n)
                        solve()
                        if solved == False:
                            grid [i][j] =0
                return 
    solved = True

def click_cell(i,j):
    cell = browser.find_element_by_css_selector('tr.game-row:nth-child(' +str(i)+') > td:nth-child('+str(j) +')') 
    cell.click()
    #cell = browser.find_element_by_css_selector('td.highlight-table:nth-child('+ str(i) +') > div:nth-child('+str(j)+')')
    #cell.send_keys('1')

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


#Main
#Variables
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

grid=[
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9] ]

solved= False
url="https://sudoku.com/pt"
dim=[0,0]


#Program
browser = webdriver.Firefox(executable_path=r'C:\Users\cppin\Desktop\Python\geckodriver.exe')
browser.get(url)
print('Browser Opened')

cookies = browser.find_element_by_css_selector('#banner-accept')
cookies.click()
print('Cookies Accepted')

html = browser.page_source
soup = BeautifulSoup(html, 'lxml')
elements = (soup.tbody).select('div.cell-value')


for j in range (9):
    for i in range (9):       
        aux=elements[j*9+i].select('svg')
        aux=str(aux)
        
        height = aux.find('height')
        width = aux.find('width')
        
        if height != -1 and width != -1:
            dim[0]= int(aux[width+len('width="')] + aux[width+len('width="')+1])
            dim[1]= int(aux[height+len('height="')] + aux[height+len('height="')+1])
        
        if aux == '[]':
            grid[j][i] = 0
        else:
            grid[j][i] = find_match(svg,dim,aux)

print(numpy.matrix(grid))
solve()
print(numpy.matrix(grid))


for i in range (1,10,1):
    for j in range (1,10,1):
        click_cell(i,j)
