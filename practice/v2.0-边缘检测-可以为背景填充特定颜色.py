import cv2
import numpy as np 

img = cv2.imread(r'C:\Users\ticao\Desktop\electronic-system-practice\photos\1.jpg')
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

blue=cv2.inRange(hsv,np.array([78,43,46]),np.array([155,255,255]))
contours, hierarchy = cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    area = cv2.contourArea(contours[i])
    if area > 200:
        cv2.drawContours(img,[contours[i]],-1,(0,255,0),-1)

showimg = cv2.resize(img,(600,800))
cv2.imshow("showimg",showimg)
cv2.waitKey(0)