from ultralytics import YOLO
import cv2

from PIL import Image
import requests

# Load model 
model=YOLO("/home/sanchay/Documents/kavach/best_new.pt")

# Results 
def get_boundbox(img):
    res = model(img,conf=0.50)
    res_plotted = res[0].plot()
    cv2.imshow("result", res_plotted)
    cv2.waitKey()
    cv2.destroyAllWindows()

# Mainn function

if __name__=='__main__':
    image=cv2.imread("/home/sanchay/Documents/kavach/face.jpg")
    get_boundbox(image)