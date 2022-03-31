# -*- coding: utf-8 -*-
from PIL import Image
import os
import xml.etree.cElementTree as ET#需要安装lxml包

#---------------------------------------------------#
#   + 通过xml文件找到所有的类别 +
#---------------------------------------------------#
def get_class_name(xml_annotations_path, class_names_path, images_path):
    xmls=os.listdir(xml_annotations_path)
    class_names_file=open(class_names_path,"wt")
    #class_names=["airplane","helicoptor","tank","ship"]#如果指定类别的名称和顺序，则按指定的顺序编号
    class_names=[]#如果类别名列表为空，则自动根据xml文件目标的名称生成类别名，并自动编号
    for xml in xmls:
        tree=ET.ElementTree(file=xml_annotations_path+xml)
        root=tree.getroot()
        line=images_path+xml.split(".")[0]+".jpg"
        for obj in root.findall("object"):
            name=obj.find("name").text
            if name not in class_names:
                class_names.append(name)
            
            box=obj.find("bndbox")
            xmin=box.find("xmin").text
            ymin=box.find("ymin").text
            xmax=box.find("xmax").text
            ymax=box.find("ymax").text

            index=str(class_names.index(name))
            line=line+" "+xmin+","+ymin+","+xmax+","+ymax+","+index
            
    for name in class_names:
        class_names_file.writelines(name+"\n")
    class_names_file.close()


if __name__ == "__main__":
    root_path = "VOCdevkit/VOC2007/"
    xml_annotations_path = root_path + "Annotations/"#一个包含xml导航文件的目录
    images_path = root_path + "JPEGImages/"#训练时图片所在的目录
    class_names_path = "classes.names"#保存类别名称
    get_class_name(xml_annotations_path, class_names_path, images_path)
    print("done!")
