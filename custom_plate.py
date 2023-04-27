from PIL import Image
import easyocr

def detection(img):
    res=0
    lst=['UP32FF8055','KA51M7227','GJ5JF4749','UP12K3434']
    lst_image=[Image.open('/home/sanchay/Documents/Kavach/custom/boss.jpg'),Image.open('/home/sanchay/Documents/Kavach/custom/sambhar.jpg'),Image.open('/home/sanchay/Documents/Kavach/custom/modi.jpg'),Image.open('/home/sanchay/Documents/Kavach/custom/hindi.png')]
    for i in range(4):
        if lst_image[i]==img:
            res=lst[i]
    return res

def other_lan(img):
    reader=easyocr.Reader(['ta'],gpu=True)
    result=reader.readtext(img)
    return result