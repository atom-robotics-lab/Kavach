import streamlit as st
import numpy as np
from PIL import Image
import custom_plate as cp
from ultralytics import YOLO

st.title(' ANPR SYSTEM ')

import requests
regions = ['mx', 'in'] 
model= YOLO("new_anpr.pt")
image=st.file_uploader("Upload file",type=['jpg','png','jpeg','mp4'])

if image is not None:
    byte=image.getvalue()
    img=Image.open(image)
    res=0#cp.detection(img)
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
    data=dict(regions=regions),  
    files=dict(upload=byte),
    headers={'Authorization': 'Token ddc92b2a61c5986da8620c4ea8640b1c1d01e71c'})
    result=response.json()['results'][0]
    st.image(img, channels="BGR")
    if res==0:
        st.text(f"Region code: {result['region']['code']}")
        st.text(f"Type: {result['vehicle']['type']}") 
        st.text(f"Plate Number: {result['plate'].upper()}")
    else :
        st.text(f"Plate Number: {res}")