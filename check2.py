import cv2
from imutils import contours
import numpy as np
from matplotlib import pyplot as plt

def get_sudo(name,size):
    img = cv2.imread(name,0)
    original = img.copy()
    #img = cv2.medianBlur(img,5)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    greymain = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    
    th2 = cv2.adaptiveThreshold(greymain,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY_INV,39,10)
    
    
    contours,heirarchy = cv2.findContours(th2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    maxarea = 0
    cnt = contours[0]
    for i in contours:
        if cv2.contourArea(i)>maxarea:
            cnt = i
            maxarea = cv2.contourArea(i)
    blank = np.zeros(img.shape,np.uint8)
    image = cv2.drawContours(blank,[cnt],-1,(255,255,255),2)
    edges = cv2.Canny(image,40,150,apertureSize = 3)
    lines = cv2.HoughLines(edges,1,np.pi/180,100)
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
            for (rho1,theta1) in created:
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
                m=abs(1/np.tan(theta))
                print(m)
                if m<1:
                    createhor.append((rho,theta))
                else:
                    createver.append((rho,theta))
                created.append((rho,theta))
                
    points=[]
    for (rho,theta) in createhor:
        for (rho1,theta1) in createver:
            if (rho,theta)!=(rho1,theta1):
                a=[[np.cos(theta),np.sin(theta)],[np.cos(theta1),np.sin(theta1)]]
                b=[rho,rho1]
                cor=np.linalg.solve(a,b)
                if list(cor) not in points:
                    points.append(list(cor))
    
                
    points.sort()
    print(points)
    if (points[0][1]>points[1][1]):
        points[0],points[1]=points[1],points[0]
    if (points[-1][1]<points[-2][1]):
        points[-1],points[-2]=points[-2],points[-1]
    
    points[1],points[2]=points[2],points[1]
    for i in points:
        images = cv2.circle(image,(int(i[0]),int(i[1])),4,(0,0,255),-1)
    pts1 = np.float32(points)
    pts2 = np.float32([[0,0],[size,0],[0,size],[size,size]])
    print(pts1)
    print(pts2)
    M = cv2.getPerspectiveTransform(pts1,pts2)
    
    warped2 = cv2.warpPerspective(blank,M,(size,size))
    img = cv2.warpPerspective(original,M,(size,size))
    return img

size=900
img = get_sudo('sudoku5.jpg',size)
thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                cv2.THRESH_BINARY_INV,39,10)
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
for cnt in contours:
    epsilon = 0.04*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    approx = cv2.convexHull(cnt)
    area = cv2.contourArea(approx)
    if area <= 9000:
        blank = cv2.drawContours(blank,[approx],-1,(255,255,255),2)

plt.subplot(121),plt.imshow(img,cmap='Greys_r')
plt.subplot(122),plt.imshow(blank,cmap='Greys_r')
plt.show()
