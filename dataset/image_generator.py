import cv2
import numpy as np
from matplotlib import pyplot as plt

fl = open("sudoku.csv","r")
sudoku = fl.readlines()
puzzles = []
for i in sudoku:
    tempquiz,tempsol = i.split(',')
    puzzles.append((tempquiz,tempsol[:-1]))
size = 900
blank = np.zeros((size,size),np.uint8)
factor = blank.shape[0]//9
for i in range(10):
    print(factor*i)
    cv2.line(blank,(0,factor*i),(blank.shape[1],factor*i),(255),2,2)
    cv2.line(blank,(factor*i,0),(factor*i,blank.shape[0]),(255),2,2)

counter = 1
x=0
y=-1
factor = blank.shape[0]//9
for (index,puzzle) in enumerate(puzzles[1:]):
    index+=1
    print(puzzle)
    ques,sol = puzzle
    print(ques,sol)
    blank_temp= blank.copy()
    y=-1
    x=0
    for num in ques:
        if (x%9)==0:
            x=0
            y+=1
        textX = int( factor*x+factor/2 )
        textY = int( factor*y+factor/2 )
        font = cv2.FONT_HERSHEY_SIMPLEX
        if num!='0':
            cv2.putText(blank_temp,num,(textX,textY),font,1.5,(255,255,255),6)
        x+=1
    cv2.imwrite("question/{}.jpg".format(index),blank_temp)
    blank_temp= blank.copy()
    y=-1
    x=0
    for num in sol:
        if (x%9)==0:
            x=0
            y+=1
        textX = int( factor*x+factor/2 )
        textY = int( factor*y+factor/2 )
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(blank_temp,num,(textX,textY),font,1.5,(255,255,255),6)
        x+=1
    cv2.imwrite("solved/{}.jpg".format(index),blank_temp)

plt.imshow(blank,cmap='Greys_r')
plt.show()
