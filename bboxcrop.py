import pandas as pd
import cv2
import numpy as np
import glob
import os


filenames = glob.glob("C:\Users\SamAl\Documents\Projects\Pupetter HTML Rendering\images\saleimages\test\00000002.jpg")
filenames.sort()
df = pd.read_csv('abnormal.csv')
im_csv_np = df.loc[:,"patientId"].values

for f in filenames:
    img = cv2.imread(f)
    img_name = f.split(os.sep)[-1]
    idx = np.where(im_csv_np == img_name)
    if idx[0].shape[0]: # if there is a match shape[0] should 1, if not 0
        for i in idx:
            name = df.loc[i]['patientId']
            start_point = (df.loc[i]['x_dis'],df.loc[i]['y_dis'])  
            end_point = (df.loc[i]['x_dis']+df.loc[i]['width_dis'],df.loc[i]['y_dis']+df.loc[i]['height_dis'])  
            crop = img[df.loc[i]['y_dis']:df.loc[i]['y_dis']+df.loc[i]['height_dis'],
                        df.loc[i]['x_dis']:df.loc[i]['x_dis']+df.loc[i]['width_dis']]
            cv2.imwrite("abnormal/crop_{0}.png".format(i), crop)