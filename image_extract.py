import pydicom as dicom
import matplotlib.pylab as plt
import cv2
import os


# specify your image path
s_dir = "./wkx_oral/s0000001"
dicom_list = os.listdir(s_dir)
dicom_list = sorted(dicom_list)
try:
    os.makedirs("./images")
except:
    pass
for img in dicom_list:
    print(img)
    if(img[-3:] == "425"):
        continue
    curr_dir = s_dir + "/" + img
    ds = dicom.dcmread(curr_dir)
    cv2.imwrite("./images/"+img+".jpg", ds.pixel_array)
