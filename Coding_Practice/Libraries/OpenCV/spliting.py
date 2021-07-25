import numpy as np
import cv2

color = cv2.imread("Detection/assets/MIT_Dome.jpg", 1)
color = cv2.resize(color, (0,0), fx=0.5, fy=0.5)
cv2.imshow("MIT", color)
print(color.shape)
height, width, channels = color.shape

b,g,r = cv2.split(color)

rgb_split = np.empty([height, width*3, 3], 'uint8')

zeros = np.zeros(b.shape, 'uint8')

rgb_split[:, :width] = cv2.merge([b,b,b])
rgb_split[:, width:width*2] = cv2.merge([g,g,g])
rgb_split[:, width*2:] = cv2.merge([r,r,r])

# more effient:
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v), axis=1)
cv2.imshow("HSV", hsv_split)

cv2.imshow("MIT Split", rgb_split)

cv2.waitKey(0)
cv2.destroyAllWindows()