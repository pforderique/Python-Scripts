'''
This is just to mess around 
'''
import cv2

def show_img(img):
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('assets/MIT_Dome.jpg', -1)
height, width = img.shape[:2]
center = (width//2, height//2)
print("Width: {1}\nHeight: {0}\nCenter: {2}".format(height, width, center))

# rectangle(img, TOP_LEFT_COOR, BOTTOM_RIGHT_COOR, color BGR, line width)
rectangle = cv2.rectangle(img, (1500, 900), (600, 400), (255, 0, 0), 2) 

# putText(img, text, BOTTOM_LEFT_COOR_START, FONT, FONT_SIZE, color BGR, line width)
text = cv2.putText(img, 'MIT Dome', (680, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 4) 

if __name__ == "__main__":
    show_img(img)