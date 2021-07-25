# Blur helps with filtering out noise
import numpy as np
import cv2

img = cv2.imread('Detection/assets/soccer_practice.jpg', 1)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
cv2.imshow("original", img)

# blur of (5,55) blurs image a lot more in the y direction
blur = cv2.GaussianBlur(img, (5,55), 0)
cv2.imshow("blurred", blur)

kernel = np.ones((5,5), 'uint8')
# pixels favor white surroundings
dilate = cv2.dilate(img, kernel, iterations=1)
# pixels favor black surroundings
erode = cv2.erode(img, kernel, iterations=1)

cv2.imshow("Dilate", dilate)
cv2.imshow("Erode", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()