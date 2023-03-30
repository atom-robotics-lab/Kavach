from ultralytics import YOLO
model= YOLO("best_new.pt")
model.predict("/home/sanchay/Documents/kavach/custom/img1.jpg")