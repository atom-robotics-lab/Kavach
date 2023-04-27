from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import requests

regions = ['mx', 'in'] 
model= YOLO("new_anpr.pt")
img=cv2.imread("/home/sanchay/Documents/Kavach/frames/img18.jpg")

res=model(img,conf=0.40)
res_plotted = res[0].plot(line_width=2)

for i in res[0].boxes.data:
    print(i)
    if int(i[5])==1:
        crop=img[int(i[1]):int(i[3]),int(i[0]):int(i[2])]
        _, im_buf_arr=cv2.imencode(".jpg", crop)
        byte= im_buf_arr.tobytes()
        response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  
        files=dict(upload=byte),
        headers={'Authorization': 'Token ddc92b2a61c5986da8620c4ea8640b1c1d01e71c'})
        result=response.json()['results']
        print(result['plate'])
        cv2.imshow("result",crop)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

