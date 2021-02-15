'''
Tutorial 2: Image Fundamentals and Manipulation

Piero Orderique
15 Feb 2021
'''

import cv2
from random import randint
#* openCV loads in image as numpy array!
img = cv2.imread('assets/MIT_Dome.jpg', -1)

#* h, w, channels --- pic is actually rep by 3D array in BGR  (NOT RGB)
print(img.shape)
'''
[
    row0: [[b00, g00, r00], [b01, g01, r01], ... ],
    row1: [[b10, g10, r10], [b11, g11, r11], ... ],
    ...
]
'''

#* Changing pixels to random 
# for i in range(300):
#     for j in range(img.shape[1]):
#         img[i][j] = [randint(0, 255), randint(0, 255), randint(0, 255)]

#* lets copy part of the image and paste it somewhere else in the image
#? tag is copying the pixels in rows 300-699, cols 400-1199
tag = img[300:700, 400:1200]
#? now paste somewhere in the image (must be same shape) (lets just move it up)
img[0:400, 400:1200] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()