# Segmentation --> converts image to binary image from src
import numpy as np
import cv2

bw = cv2.imread('Detection/assets/soccer_practice.jpg', 0)
bw = cv2.resize(bw, (0,0), fx=0.5,fy=0.5)
height, width = bw.shape[0:2]
cv2.imshow("Original BW", bw)

binary = np.zeros([height,width,1], 'uint8')

# set a threshold
threshold = 85

#slow
for row in range(0, height):
    for col in range(0, width):
        binary[row][col] = 255 if bw[row][col] > threshold else 0
# cv2.imshow("Slow Binary", binary)

# cv2's version
ret, threshold = cv2.threshold(bw, threshold, 255,cv2.THRESH_BINARY)
cv2.imshow("thresh", threshold)


# ADAPTIVE THRESHOLD -- works best!!! segment out exactly what you need!
thresh_adapt = cv2.adaptiveThreshold(bw, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Adaptive", thresh_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()