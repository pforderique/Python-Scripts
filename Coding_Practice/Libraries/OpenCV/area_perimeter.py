# Area, Perimeter, and Centroids
import numpy as np
import cv2

img = cv2.imread('Detection/assets/stop_sign.jpg', 1)
# img = cv2.resize(img, (0,0), fx=0.5,fy=0.5)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Binary", thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img2 = img.copy()
index = -1
thickness = 4
color = (255, 0, 255)

objects = np.zeros([img.shape[0], img.shape[1], 3], 'uint8')
for c in contours:
    cv2.drawContours(objects, [c], index, color, -1) # -1 means fill in 

    area = cv2.contourArea(c) # in pixels^2
    perimeter = cv2.arcLength(c, True)
    
    # centroid = "center of mass"
    try:
        M = cv2.moments(c)
        cx = int( M['m10'] / M['m00'] )
        cy = int( M['m01'] / M['m00'] )
        cv2.circle(objects, (cx, cy), 4, (255,0,0), -1)
    except ZeroDivisionError:
        pass
    print(f'Area: {area}, Perimeter: {perimeter}')

cv2.drawContours(img2, contours, index, color, thickness)
cv2.imshow("Contours", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()