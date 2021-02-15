'''
This is just to mess around 
'''
import cv2

img = cv2.imread('assets/MIT_Dome.jpg', -1)
print("Height: {0}\nWidth: {1}".format(img.shape[0], img.shape[1]))