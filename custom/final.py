import cv2
from ultralytics import YOLO

model=YOLO("/home/sanchay/Documents/kavach/new_anpr.pt")
img=cv2.imread("/home/sanchay/Documents/kavach/frame4.jpg")
res = model(img,conf=0.50)
res_plotted = res[0].plot()
cv2.imshow("result", res_plotted)
cv2.waitKey()
cv2.destroyAllWindows()

