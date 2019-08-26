#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-28T06:52:38.406Z
# @Author  : CarryHJR

import numpy as np
import cv2

######################################################################
# 原始图像real
real = cv2.imread(r'C:\Users\ticao\Desktop\electronic-system-practice\photos\1.jpg')
cv2.namedWindow("real",0)
cv2.imshow("real", real)

# 前景图像
cv2.namedWindow("Image",0)
gray = cv2.cvtColor(real, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
img = cv2.threshold(blurred, 199, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Image", img)

# 2次腐蚀,3次膨胀
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# img = cv2.erode(img, kernel, iterations=2)
# img = cv2.dilate(img, kernel, iterations=3)


cnts = cv2.findContours(img.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0]
cv2.drawContours(real, cnts, -1, (0, 255, 0), 2)
# # loop over the contours
# for c in cnts:
#     cv2.drawContours(real, [c], -1, (0, 255, 0), 2)
# cv2.imshow("real", real)
# cv2.drawContours(real, cnts, -1, (0, 255, 0), 2)
cv2.namedWindow("contours.png",0)
cv2.imshow('contours.png', real)

while (1):

    # cv2.imwrite('contours.png', real)

    # https://stackoverflow.com/questions/37912928/fill-the-outside-of-contours-opencv
    # 全黑
    # mask = np.zeros(real.shape).astype(real.dtype)
    # # 将contours里填充白色
    # color = [255, 255, 255]
    # cv2.fillPoly(mask, cnts, color)
    # # mask与real相与
    # result = cv2.bitwise_and(real, mask)

    # # 最后结果reult
    # cv2.namedWindow("result",0)
    # cv2.imshow('result', result)
    # cv2.waitKey(1)
    ###################################################################
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
