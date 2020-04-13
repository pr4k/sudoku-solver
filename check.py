import cv2
import matplotlib.pyplot as plt

img = cv2.imread('sudoku.jpeg')
#ret,thresh = cv2.threshold(img,127,255,0)
#contours,hierarchy = cv2.findContours(thresh, 1, 2)
#
#cnt = contours[0]
#M=cv2.convexHull(cnt)
#
#print (M)

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
grey = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
print(grey)
_,binary = cv2.threshold(grey,127,255,cv2.THRESH_BINARY)
print(binary)
contours,heirarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

image = cv2.drawContours(img,contours,-1,(0,255,0),2)
plt.imshow(image)
plt.show()
