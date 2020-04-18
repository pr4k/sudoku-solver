import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

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

fl = open("sudoku.csv","r")
sudoku = fl.readlines()
puzzles = []
for i in sudoku:
    tempquiz,tempsol = i.split(',')
    puzzles.append((tempquiz,tempsol[:-1]))
index = [0,0,0,0,0,0,0,0,0,0]
for (_,puzzle) in enumerate(puzzles[1:]):
    ques,sol = puzzle
    for num in ques:
        if index[int(num)]<15000:
            index[int(num)]+=1
            blank = np.zeros((28,28),np.uint8)
            textX = 11 + (random.randint(-5,5)) 
            textY =  15 + (random.randint(-5,5))
            font = cv2.FONT_HERSHEY_SIMPLEX
            if num!='0':
                cv2.putText(blank,num,(textX,textY),font,0.5,(255,255,255),1)
                blank = sp_noise(blank,0.01)
                cv2.imwrite("{}/{}.jpg".format(int(num),index[int(num)]),blank)
                print("writing {}/{}.jpg".format(int(num),index[int(num)]))
            else:
                blank = sp_noise(blank,0.001)
                cv2.imwrite("0/{}.jpg".format(index[int(num)]),blank)
                print("writing 0/{}.jpg".format(index[int(num)]))
        else:
            pass 

