# created by Huang Lu
# 28/08/2016 14:46:31 
# Department of EE, Tsinghua Univ.

import cv2
import numpy as np

img = cv2.imread(r'C:\Users\ticao\Desktop\electronic-system-practice\photos\1.jpg')
img2 = cv2.imread(r'C:\Users\ticao\Desktop\electronic-system-practice\photos\mask.jpg')
img3 = cv2.imread(r'C:\Users\ticao\Desktop\electronic-system-practice\photos\back.jpg')

# set blue thresh
lower_blue=np.array([78,43,46])
upper_blue=np.array([110,255,255])

while(1):
    # get a frame and show
    cv2.namedWindow("Image",0)
    cv2.imshow('Image', img)

    # # change to hsv model
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # # get mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.namedWindow("Mask",0)
    cv2.imshow('Mask', mask)

    # 
    mask_inv = cv2.bitwise_not(mask)
    cv2.namedWindow("Maskinv",0)
    cv2.imshow('Maskinv', mask_inv)

    # detect blue
    res = cv2.bitwise_and(img,img,mask=mask_inv)
    cv2.namedWindow("Result",0)
    cv2.imshow('Result', res)

    # Put logo in ROI and modify the main image
    # dst = cv2.add(mask,res)
    # cv2.namedWindow("test",0)
    # cv2.imshow('test', dst)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

