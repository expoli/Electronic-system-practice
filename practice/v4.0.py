import cv2
import numpy as np 

#设置人所在的位置和人的大小
people_height = 1200     #人像缩放高度
people_width = 800      #人像缩放宽度
people_loc_x = 500      #人像定位（从左上角开始）
people_loc_y = 300      

#打开人像图片
img = cv2.imread('C:/Users/LSB/Desktop/electronic-system-practice/photos/1.jpg')

#打开背景图片
img_background = cv2.imread('C:/Users/LSB/Desktop/electronic-system-practice/photos/3.jpg')

#根据背景图片大小创建一个三通道图像，且全部为蓝色（消除色）
result = np.zeros((int(img_background.shape[0]),int(img_background.shape[1]),3),np.uint8)
result[:,:,0],result[:,:,1],result[:,:,2] = 255,0,0

#人像转换成HSV,再通过inRange获取蓝色区域
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
blue=cv2.inRange(hsv,np.array([78,43,46]),np.array([155,255,255]))
#蓝色区域进行描边
#边缘检测
contours, hierarchy = cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#排除一些小蓝点
for i in range(len(contours)):
    area = cv2.contourArea(contours[i])
    if area > 200:
        #填充为蓝色
        cv2.drawContours(img,[contours[i]],-1,(255,0,0),-1)
        pass

#人像缩放到指定大小
people = cv2.resize(img,(people_width,people_height))
#人像放置到结果图片中
result[people_loc_y:people_loc_y+people_height,people_loc_x:people_loc_x+people_width] = people

#对人像的蓝色进行选中
background = cv2.inRange(result,np.array([255,0,0]),np.array([255,0,0]))
#再通过蓝色区域和背景图片与运算获得需要的背景
tmp_back = cv2.bitwise_and(img_background,img_background,mask=background)
#人像的蓝色区域反选，并与人像图片与运算获得需要的人像
tmp_people = cv2.bitwise_and(result,result,mask=cv2.bitwise_not(background))
#和运算，二者相加（因为空白的地方是黑色【0，0，0】）
result = cv2.add(tmp_back,tmp_people)

#为了显示方便缩放一下结果
img_result = cv2.resize(result,(600,800))
cv2.imshow("hole",img_result)
cv2.waitKey(0)
