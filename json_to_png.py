import base64
import json
import os
import os.path as osp
import numpy as np
import PIL.Image
from labelme import utils

# labelme版本是3.16.7,版本不同可能会报错
# 视情况使用json文件对应的labelme版本

if __name__ == '__main__':
    count = os.listdir("./before")  # 原来json的文件夹位置
    jpgs_path = "jpg"  #生成jpg的文件夹位置
    pngs_path = "png"  #生成png的文件夹位置
    classes = ["_background_","kongpao"]   #按自定义标注的分类修改

    # 按1,2,3... 而不是1,10,100读取
    count.sort(key=lambda x: int(x.split('.')[0]))

    if not os.path.exists(jpgs_path):
        os.mkdir(jpgs_path)
    if not os.path.exists(pngs_path):
        os.mkdir(pngs_path)

    for i in range(0, len(count)):
        path = os.path.join("./before", count[i])    #按实际情况修改

        if os.path.isfile(path) and path.endswith('json'):
            data = json.load(open(path))
            
            if data['imageData']:
                imageData = data['imageData']
            else:
                imagePath = os.path.join(os.path.dirname(path), data['imagePath'])
                with open(imagePath, 'rb') as f:
                    imageData = f.read()
                    imageData = base64.b64encode(imageData).decode('utf-8')

            img = utils.img_b64_to_arr(imageData)
            label_name_to_value = {'_background_': 0}
            for shape in data['shapes']:
                label_name = shape['label']
                if label_name in label_name_to_value:
                    label_value = label_name_to_value[label_name]
                else:
                    label_value = len(label_name_to_value)
                    label_name_to_value[label_name] = label_value
            
            # label_values must be dense
            label_values, label_names = [], []
            for ln, lv in sorted(label_name_to_value.items(), key=lambda x: x[1]):
                label_values.append(lv)
                label_names.append(ln)
            assert label_values == list(range(len(label_values)))
            
            lbl = utils.shapes_to_label(img.shape, data['shapes'], label_name_to_value)
            
                
            PIL.Image.fromarray(img).save(osp.join(jpgs_path, count[i].split(".")[0]+'.jpg'))

            new = np.zeros([np.shape(img)[0],np.shape(img)[1]])
            for name in label_names:
                index_json = label_names.index(name)
                index_all = classes.index(name)
                new = new + index_all*(np.array(lbl) == index_json)

            utils.lblsave(osp.join(pngs_path, count[i].split(".")[0]+'.png'), new)
            print('Saved ' + count[i].split(".")[0] + '.jpg')
            print('Saved ' + count[i].split(".")[0] + '.png')

