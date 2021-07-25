import numpy as np
import cv2

img = cv2.imread('Detection/assets/faces.jpg', 1)
img = cv2.resize(img, (0,0), fx=0.5,fy=0.5)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)

hsv_split = np.concatenate((h,s,v),axis=1) #horizontally
cv2.imshow("Split HSV", hsv_split)

# everything that is in the saturation channel that is 40 or 
# higher will appear as white (255)
ret, min_sat = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY)
cv2.imshow("Sat Filter", min_sat)

# Inverse the threhold -- hue value of 0 to 15 appears white
ret, max_hue = cv2.threshold(h,15,255, cv2.THRESH_BINARY_INV)
cv2.imshow("Hue Filter", max_hue)

# combine both filters
final = cv2.bitwise_and(min_sat, max_hue)
cv2.imshow("Final", final)
cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()