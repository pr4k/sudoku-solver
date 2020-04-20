import cv2
from imutils import contours as cnt_sort
import numpy as np
from matplotlib import pyplot as plt
import random

def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output
def create_original(img):
    original = img.copy()
    
    thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                    cv2.THRESH_BINARY_INV,39,10)
    thresh1 = thresh.copy()
    kernel = np.ones((1,1),np.uint8)
    #thresh = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel)
    #thresh = cv2.dilate(thresh,kernel,iterations=3)
    kernel = np.ones((1,10),np.uint8)
    thresh = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)
    kernel = np.ones((10,1),np.uint8)
    thresh = cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel)
    
    #contours,heirarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    thresh = cv2.bitwise_not(thresh)
    contours,heirarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    blank = np.zeros(img.shape,np.uint8)
    finalContours = []
    for cnt in contours:
        epsilon = 0.04*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)
        approx = cv2.convexHull(cnt)
        area = cv2.contourArea(approx)
        if area <= 9000:
            finalContours.append(approx)
    if len(finalContours)>0:
        sudoku_rows,_ = cnt_sort.sort_contours(finalContours,method="left-to-right")
        kernel = np.ones((3,3),np.uint8)
        thresh1 = cv2.erode(thresh1,kernel,iterations=1)
        blank_base = blank.copy()
        for c in sudoku_rows:
            blank = cv2.drawContours(blank,[c],-1,(255),-1)
            blank_base = cv2.drawContours(blank_base,[c],-1,(255),-1)
            blank = cv2.bitwise_and(thresh1,blank,mask=blank)
        
        #print((sudoku_rows))
        #for (i,c) in enumerate(sudoku_rows,1):
        #    blnk = blank
        #    blnk = cv2.drawContours(blnk,[c],-1,(255,255,255),-1)
        #    cv2.imwrite("images/{}.jpg".format(i),blnk)
        kernel = np.ones((5,1),np.uint8)
        blank = cv2.erode(blank,kernel,iterations=1)
        kernel = np.ones((6,6),np.uint8)
        blank = cv2.morphologyEx(blank,cv2.MORPH_CLOSE,kernel)
        kernel = np.ones((1,5),np.uint8)
        blank = cv2.erode(blank,kernel,iterations=1)
        kernel = np.ones((9,9),np.uint8)
        blank = cv2.morphologyEx(blank,cv2.MORPH_CLOSE,kernel)
        kernel = np.ones((6,6),np.uint8)
        blank = cv2.dilate(blank,kernel,iterations=1)
        factor = blank.shape[0]//9
        sudoku = []
        
        for i in range(10):
            print(factor*i)
            cv2.line(blank,(0,factor*i),(blank.shape[1],factor*i),(255),2,2)
            cv2.line(blank,(factor*i,0),(factor*i,blank.shape[0]),(255),2,2)
        
        
    plt.subplot(121),plt.imshow(original,cmap='Greys_r')
    plt.subplot(122),plt.imshow(blank,cmap='Greys_r')
    plt.show()
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
for (index,puzzle) in enumerate(puzzles[1:3]):
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
        font = cv2.FONT_HERSHEY_PLAIN
        if num!='0':
            cv2.putText(blank_temp,num,(textX,textY),font,3.3,(255,255,255),3)
        x+=1
    create_original(blank_temp)

