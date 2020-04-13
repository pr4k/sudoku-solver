import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('sudoku3.jpg',0)
#img = cv2.medianBlur(img,5)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
grey = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

th2 = cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY_INV,39,10)


contours,heirarchy = cv2.findContours(th2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
maxarea = 0
cnt = contours[0]
for i in contours:
    if cv2.contourArea(i)>maxarea:
        cnt = i
        maxarea = cv2.contourArea(i)
#x,y,_ = img.shape
#pts1 = np.float32([[0,0],[x,0],[0,y],[x,y]])
#pts2 = np.float32(box)
#M = cv2.getPerspectiveTransform(pts2,pts1)
#dst = cv2.warpPerspective(img,M,(600,600))
blank = np.zeros(img.shape,np.uint8)
#blank2 = np.zeros(img.shape,np.uint8)
image = cv2.drawContours(blank,[cnt],-1,(255,255,255),2)
edges = cv2.Canny(image,40,150,apertureSize = 3)
#minlinelen = 1000
#maxlinegap = 10
lines = cv2.HoughLines(edges,1,np.pi/180,100)
#print(len(lines[0]),lines)
print(len(lines))
createhor = []
createver = []
created = []
anglediff=10
rhodiff=10
flag=0
count = 2

for line in lines:
    for (rho,theta) in line:
        flag=0
        for (rho1,theta1,_) in created:
            if abs(rho-rho1)<rhodiff and abs(theta-theta1)<anglediff:
                flag=1
                
        if flag==0:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            d = np.linalg.norm(np.array((x1,y1,0))-np.array((x2,y2,0)))
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
            created.append((rho,theta,abs(1/np.tan(theta))))
            
def last(n):
    return n[-1]
created = sorted(created,key= last)
points = []
createhor = created[0:2]
createver = created[-2:]
print(createhor)
print(createver)
for (rho,theta,_) in createhor:
    for (rho1,theta1,_) in createver:
        if (rho,theta)!=(rho1,theta1):
            a=[[np.cos(theta),np.sin(theta)],[np.cos(theta1),np.sin(theta1)]]
            b=[rho,rho1]
            cor=np.linalg.solve(a,b)
            if list(cor) not in points:
                points.append(list(cor))

            
print(len(points))
for i in points:
    images = cv2.circle(image,(int(i[0]),int(i[1])),4,(0,0,255),-1)
pts1 = np.float32(points)
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,300))

#plt.imshow(blank2)
#image = cv2.Canny(img,100,200)
plt.imshow(dst)
plt.show()
