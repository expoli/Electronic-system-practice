import cv2
import numpy as np

img = cv2.imread(r'C:\Users\LSB\Desktop\electronic-system-practice\photos\1.jpg')
img_bg = cv2.imread(r'C:\Users\LSB\Desktop\electronic-system-practice\photos\back_test.jpg')

'''
x, y = img.shape[0:2]
img = cv2.resize(img, (int(y / 2), int(x / 2)))
'''

img = cv2.resize(img, (0, 0), fx=0.25, fy=0.25, interpolation=cv2.INTER_NEAREST)

lower_bgd_clr = np.array([78,43,46])
upper_bgd_clr = np.array([110,255,255])

#cap = cv2.VideoCapture(0)
#ret, img = cap.read()

# 反转颜色
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 去除蓝色部分
mask = cv2.inRange(hsv, lower_bgd_clr, upper_bgd_clr)
#mask = cv2.GaussianBlur(mask,(3,3),0)
# 腐蚀与膨胀
#mask = cv2.erode(mask, None, iterations = 1)
mask = cv2.dilate(mask, None, iterations= 1)
print(img_bg.shape)
rows, cols = mask.shape
# 切割背景图
img_bg = img_bg[0:rows, 0:cols]
print(img_bg.shape,mask.shape)
# 按位与
img_fg = cv2.bitwise_and(img_bg,img_bg,mask = mask)
# 反转mask
mask_inv = cv2.bitwise_not(mask)
# 按位与
img_fg2 = cv2.bitwise_and(img,img,mask = mask_inv)
# 合成
res = img_fg+img_fg2

#mask = cv2.inRange(res, lower_bgd_clr, upper_bgd_clr)
cv2.imshow('img',img)
#cv2.imshow('hsv',hsv)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

while True:

    if cv2.waitKey(0)&0xFF == ord('q'):
        break