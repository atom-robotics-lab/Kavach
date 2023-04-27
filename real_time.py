import streamlit as st
import numpy as np
from PIL import Image
import custom_plate as cp
import cv2
from ultralytics import YOLO
import tempfile
import shutil

model=YOLO("version_4.pt")

import requests
regions = ['mx', 'in'] 
cap=cv2.VideoCapture("/home/sanchay/Documents/Kavach/wp.mp4")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
   
size = (frame_width, frame_height)
file_out = tempfile.NamedTemporaryFile(suffix='.avi')

result = cv2.VideoWriter(file_out.name, 
                        cv2.VideoWriter_fourcc(*'MJPG'),
                        10, size)
while(cap.isOpened()):
    _,frame=cap.read()
    if _==True:
        res = model(frame,conf=0.25)
        res_plotted = res[0].plot(line_width=2)
        result.write(res_plotted)
        cv2.imshow("result", res_plotted)
            # Press Q on keyboard to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
  
# Break the loop
    else:
        break  
# When everything done, release
# the video capture object
cap.release()
cv2.destroyAllWindows()
print(file_out.name)
shutil.copy(file_out.name,'temp.avi')