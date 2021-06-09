'''
Tutorial 7: Template Matching!

Piero Orderique
09 June 2021

Notes:
>>> Template image must be veryyyy close to size to how it appears in original image (pixel wise)
'''

import numpy as np
import cv2

img = cv2.resize(cv2.imread('Detection/assets/soccer_practice.jpg', 0), (0,0), fx=0.9, fy=0.9) # load in grayscale
template = cv2.resize(cv2.imread('Detection/assets/shoe.png', 0), (0,0), fx=0.9, fy=0.9) # load in grayscale

h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    #* performs a convolution -- takes the template and slides it around source and tells us how close of a match it is to that region
    result = cv2.matchTemplate(img2, template, method) 

    #* gets the min/max val in the array and thier location
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # these two methods use MIN value as best match
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: 
        location = min_loc
    else: 
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('match',img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
