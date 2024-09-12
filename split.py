#This takes the 200 sale pages and cuts them into 4 smaller photos 

import json
import cv2
import numpy as np
import csv
from PIL import Image



for i in range(4):
  img = cv2.imread(str(i)+'r.png')
  height, width, channels = img.shape
  sections = int(height/7180)
  inpu = i
  for j in range(sections+1):
    interval = 7180
    current = 0
    crop_img = img[current:interval, 0:800]
    cv2.imwrite("{}{}r.png".format(inpu, j), crop_img)
    interval += 7180
    current += 7180
    im1 = Image.open(r'C:\Users\SamAl\Documents\Projects\Pupetter HTML Rendering/' + str(inpu) + str(j) + 'r.png')
    im = im1.convert('RGB')
    im.save(r'C:\Users\SamAl\Documents\Projects\Pupetter HTML Rendering\cropped\crop_' + str(inpu) + str(j)  + '.jpg')

