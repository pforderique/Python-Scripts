# edge detections looks for where 

import numpy as np
import cv2

img = cv2.imread("Detection/assets/stop_sign.jpg", 1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# extract all pixels with hue of 25 or less (bc of inverse)
res, thresh = cv2.threshold(hsv[:,:,0], 25, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh", thresh)

# Canny Edges algo
edges = cv2.Canny(img, 100, 70)
cv2.imshow("Canny", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()