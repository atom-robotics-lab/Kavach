import cv2
import numpy as np
from PIL import Image

import requests
regions = ['mx', 'in'] 
# with open('/home/sanchay/Documents/kavach/number plates/img1.jpg', 'rb') as fp:
#     response = requests.post(
#         'https://api.platerecognizer.com/v1/plate-reader/',
#        data=dict(regions=regions),  
#        files=dict(upload=fp),
#        headers={'Authorization': 'Token ddc92b2a61c5986da8620c4ea8640b1c1d01e71c'})
#     result=response.json()["results"][0]
#     print(result['plate'])


#    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
#    opencv_image = cv2.imdecode(file_bytes, 1)
with open('/home/sanchay/Documents/kavach/number plates/img1.jpg','rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
    data=dict(regions=regions),  
    files=dict(upload=fp),
    headers={'Authorization': 'Token ddc92b2a61c5986da8620c4ea8640b1c1d01e71c'})
    result=response.json()['results'][0]
    print(result['plate'])
    print(result['region']['code'])
    print(result['vehicle']['type']) 
