import os

from PIL import Image
import math
import operator
import matplotlib.pyplot as plt
from functools import reduce

flag = "jpg"

if flag == "jpg":
    json_file = 'C:\\Users\\admin\\Desktop\\dataset\\jpg3'
    alist = os.listdir(json_file)
    for i in range(0, len(alist)):
        path = os.path.join(json_file, alist[i])
        im2 = Image.open(path)
        im2 = im2.rotate(90) #每次翻转后修改
        # im2.save(os.path.join("./jpgfz", alist[i]))
        save_path = "./jpgfz/" + str(i+1+181) + ".jpg"  #每次翻转后修改名称
        im2.save(save_path)
        print(i+1)

if flag == "png":
    json_file = 'C:\\Users\\admin\\Desktop\\dataset\\png3'
    alist = os.listdir(json_file)
    for i in range(0, len(alist)):
        path = os.path.join(json_file, alist[i])
        im2 = Image.open(path)
        im2 = im2.rotate(90)
        save_path = "./pngfz/" + str(i+1+181) + ".png"
        im2.save(save_path)
        print(i+1)

