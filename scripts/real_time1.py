import streamlit as st
import numpy as np
from PIL import Image
import custom_plate as cp
import cv2
from ultralytics import YOLO

model=YOLO("/home/sanchay/Documents/kavach/new_anpr.pt")

import requests
regions = ['mx', 'in'] 
cap=cv2.VideoCapture("/home/sanchay/Documents/kavach/frame4.mp4")

while(cap.isOpened()):
    _,frame=cap.read()
    if _==True:
        res = model(frame,conf=0.40)
        res_plotted = res[0].plot(line_width=2)
        cv2.imshow("result", res_plotted)
            # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
  
# Break the loop
    else:
        break
  
# When everything done, release
# the video capture object
cap.release()
  
# Closes all the frames
cv2.destroyAllWindows()
