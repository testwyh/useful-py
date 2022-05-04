import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

# base_dir = "./test"  #要二值化的图片的原文件夹位置
# output_dir = './output/'  #二值化处理后存放的文件夹位置
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)
#
# # 图片名先转化为int后分类（sort）
# # 按顺序读取图片，这样保证是1,2,3...而不是1,10,11...
# filelist = os.listdir(base_dir)
# filelist.sort(key=lambda x: int(x.split('.')[0]))
#
# i = 1
# for i in range(0, len(filelist)):
#     path = os.path.join(base_dir, filelist[i])
#
#     img0 = cv2.imread('test.jpg', cv2.IMREAD_COLOR) #读取格式为BGR
#     img = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB) #转换为RGB
#     gray = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE) #转换为灰度图
#
#     '''
#     简单二值化
#     最后一项0,1,2,3,4代表不同模式
#     '''
#     ret, mask = cv2.threshold(img, 230, 255, 0)
#
#     '''
#     自适应阈值二值化
#     '''
#     th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 0, 11, 2)
#     th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 0, 11, 2)
#
#     '''
#     Ostu阈值二值化
#     '''
#     ret2, ostu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#
#     save_path = output_dir + str(i+1) + '.jpg'  #保存至另一文件夹
#     cv2.imwrite(save_path, mask)
#     print('图片 %s' % (i+1) )

# cv2.imread读取出来图片的格式是BGR与常规的彩色图像的格式（RGB）相反，一定要留意!
img0 = cv2.imread('test.jpg', cv2.IMREAD_COLOR) #读取格式为BGR
img = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB) #转换为RGB
gray = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE) #转换为灰度图
ret, mask = cv2.threshold(gray, 230, 255, 0)
th1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 0, 11, 2)
th2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 0, 11, 2)
ret2, ostu = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.imshow('mask',mask)
cv2.imshow('th1',th1)
cv2.imshow('th2',th2)
cv2.imshow('ostu',ostu)
cv2.waitKey(0)
output_dir = './output/'  #处理后存放的文件夹位置
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
cv2.imwrite(output_dir+'gray.jpg',gray)
cv2.imwrite(output_dir+'mask.jpg',mask)
cv2.imwrite(output_dir+'th1.jpg',th1)
cv2.imwrite(output_dir+'th2.jpg',th2)
cv2.imwrite(output_dir+'ostu.jpg',ostu)

