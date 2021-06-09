'''
Tutorial 1: Loading, editing, writing

Piero Orderique
15 Feb 2021
'''

import cv2

'''read in image 
    -1: normal, ignore trans #default
     0: grayscale
     1: loads as such including alpha channel
'''
img = cv2.imread('Detection/assets/MIT_Dome.jpg', 0)

''' Resizing, rotating, etc '''
#* Resize by pixel
# img = cv2.resize(img, (400, 400))

#* OR to resize by scaling (by half in this case)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

#* ROTATE 
# img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

#* WRITE IMAGE (save)
cv2.imwrite('Detection/assets/BW_MIT_Dome.png', img)

'''
load image in a window. Set window name as first arg
wait at most (0=infinity) time for user to click any key
destroy every window
'''
cv2.imshow('Image Window Name Here', img)
cv2.waitKey(0)
cv2.destroyAllWindows()