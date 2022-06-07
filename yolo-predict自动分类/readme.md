**更新时间：**
2022.6.7

**版本：**
3.0

**注意：**
运行前需检查voc_classess.txt是否正确！

如果不正确程序会出现mismatch报错。

**设置：**
在yolo_predict2.py中，根据自己需要修改 confidence

在predict2.py中，根据自己需要修改 confidence_num


**输出：**

实现了对yolo预测出的图片分类至三个文件夹，并生成txt

----------------------------------------
0.5_img_out_NEO
0.5_img_out_NONNEO
0.5_img_out_fail   
0.5_predict.txt
