import streamlit as st
import numpy as np
from PIL import Image
import custom_plate as cp
from ultralytics import YOLO
import cv2 

st.title(' ANPR SYSTEM ')

import requests
regions = ['mx', 'in'] 
model= YOLO("new_anpr.pt")
image=st.file_uploader("Upload file",type=['jpg','png','jpeg','mp4'])

plates=[]

if image is not None:
    file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    new=Image.open(image)
    flag=cp.detection(new)
    if flag==0:
        res=model(img,conf=0.50)
        res_plotted = res[0].plot(line_width=2)
        for i in res[0].boxes.data:
            if int(i[5])==1:
                crop=img[int(i[1]):int(i[3]),int(i[0]):int(i[2])]
                _, im_buf_arr=cv2.imencode(".jpg", crop)
                byte= im_buf_arr.tobytes()
                response = requests.post(
                'https://api.platerecognizer.com/v1/plate-reader/',
                data=dict(regions=regions),  
                files=dict(upload=byte),
                headers={'Authorization': 'Token ddc92b2a61c5986da8620c4ea8640b1c1d01e71c'})   
                result=response.json()['results'][0]
                plates.append(result['plate'].upper())
        st.image(res_plotted, channels="BGR")        
        st.image(crop, channels="BGR")
        for i in plates:
            st.text(f"Plate Number: {i}\n")
    else:
        st.image(img, channels="BGR")        
        st.text(f"Plate Number: {flag}")