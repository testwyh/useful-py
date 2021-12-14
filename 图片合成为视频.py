import os
import cv2

path = 'ALL_JPEG/'  # 原图片的路径
filelist = os.listdir(path)

fps = 3  # 视频每秒帧数
size = (640, 480)  # 需要转为视频的图片的尺寸，图片的尺寸多大，就写多大,例如:t1.jpg大小为480*640 （480,640）
# 可以使用cv2.resize()进行修改

# 视频的名称为VideoTest1，格式为.avi
video = cv2.VideoWriter("VideoOUT.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
# 视频保存在当前目录下

for item in filelist:
    if item.endswith('.jpg'):
        # 找到路径中所有后缀名为.jpg的文件，可以更换为.png或其它
        item = path + item
        img = cv2.imread(item)
        video.write(img)

video.release()
cv2.destroyAllWindows()