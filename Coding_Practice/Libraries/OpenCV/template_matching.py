# Template Matching Limitations:
# Not scale invariant
# Not rotation invariant
import numpy as np
import cv2

template = cv2.imread('Detection/assets/ball.png', 0)
img = cv2.imread('Detection/assets/soccer_practice.jpg', 0)
# img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

cv2.imshow("template", template)
cv2.imshow("original", img)

result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
# get the max brightness of the resulting img
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(max_val, max_loc)
cv2.circle(result, max_loc, 15, 255, 2)

cv2.imshow("matching", result)

cv2.waitKey(0)
cv2.destroyAllWindows()