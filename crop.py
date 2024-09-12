#First step after getting detection results: crop the bounding boxes into individual photos

import json
import cv2
import numpy as np
import csv

with open('result(2).json') as f:  #Enter file path for JSON file
  data = json.load(f)   #list

dict1 = data[0]  #dict

objlist = dict1['objects']  #list

bbox = []
for item in objlist:
    dict2 = item['relative_coordinates']
    x1 = dict2['center_x']
    y1 = dict2['center_y']
    w1 = dict2['width']
    h1 = dict2['height']
    list1 = [x1 , y1 , w1 , h1]
    bbox.append(list1)

img = cv2.imread('salecrops\gpus\crop_21.jpg')  #<--- Parameter: Enter file path for Image

for idx, bbox in enumerate(bbox):
    x2 = bbox[0]
    y2 = bbox[1]
    w2 = bbox[2]
    h2 = bbox[3]
    height, width, channels = img.shape
    x = int(x2 * width)
    y = int(y2 * height)
    w = int(w2 * width)
    h = int(h2 * height)
    crop_img = img[int(y-h/2):int(y+h/2), int(x-w/2):int(x+w/2)]
    cv2.imwrite("textbox_{0}.jpg".format(idx), crop_img)



