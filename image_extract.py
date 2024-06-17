import pydicom as dicom
from PIL import Image
import numpy as np
import os

s_dir = "./s0000001"
dicom_list = os.listdir(s_dir)
dicom_list = sorted(dicom_list)
try:
    os.makedirs("./images")
except:
    pass
for img in dicom_list:
    if(img[-3:] == "425"):
        break
    curr_dir = s_dir + "/" + img
    ds = dicom.dcmread(curr_dir)
    curr_image = ds.pixel_array.astype(float)
    scaled_image = np.uint8((np.maximum(curr_image,0) / curr_image.max()) * 255.0)
    im = Image.fromarray(scaled_image)
    im.save("./images/"+img+".png")
