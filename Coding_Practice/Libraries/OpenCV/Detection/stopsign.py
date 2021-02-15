'''
Image Recognition
Geeks For Geeks

Piero Orderique
15 Feb 2021
'''
import cv2 
from matplotlib import pyplot as plt 

IMAGE_PATH = "assets/stop_sign.jpg"

def main():
    # load image and print characteristics
    img = cv2.imread(IMAGE_PATH) 
    height, width = img.shape[:2]
    center = (width//2, height//2)
    print("Width by Height: {1} x {0}\nCenter: {2}".format(height, width, center))

    # OpenCV opens images as BRG but we want it as RGB and grayscale  
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

    # Haar Cascade Classifiers are rapidly trained using a lot of positive and negative images
    stop_data = cv2.CascadeClassifier('stop_data.xml') 
    # detectMultiScale() function of OpenCV to recognize big signs as well as small ones
    # Use minSize because we're not bothering with extra-small dots that would look like STOP signs 
    found = stop_data.detectMultiScale(img_gray, minSize =(20, 20)) 

    # Don't do anything if there's no sign 
    amount_found = len(found) 
    if amount_found != 0: 

        # There may be more than one sign in the image 
        for (x, y, width, height) in found: 

            # We draw a rectangle around every recognized sign 
            cv2.rectangle(img_rgb, (x, y), (x + height, y + width), (0, 0, 255), 4) 

    # Creates the environment of the picture and shows it 
    plt.subplot(1, 1, 1) 
    plt.title('Stop Signs')
    plt.imshow(img_rgb) 
    plt.show() 

if __name__ == "__main__":
    main()