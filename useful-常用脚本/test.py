# coding:utf-8
import os
import pandas as pd

#######################
# 修改以下三项：
path = './png2/'  # 要改名的文件夹
output_dir = './png3/'  #重命名后存放的文件夹
txt_dir = 'name.txt'   # txt文件夹
#######################

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

filelist = os.listdir(path)
filelist.sort(key=lambda x: int(x.split('.')[0]))

list = pd.read_csv(txt_dir, sep='\s+',
                   encoding='utf-8',
                   index_col=0,
                   names=['name','name_num'])
# list.index +=1

#print(list)
#print(list['name']+list['name_num'])

for i in range(1000,len(list)):
    print(list.iloc[i,0]+list.iloc[i,1])