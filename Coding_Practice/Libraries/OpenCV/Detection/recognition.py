'''
Image Recognition
Geeks For Geeks

Piero Orderique
15 Feb 2021
'''
import cv2 
from matplotlib import pyplot as plt 

IMAGE_PATH = "/assets/MIT_Dome.jpg"

def main():
    img = cv2.imread(IMAGE_PATH, 0) 

    # OpenCV opens images as BRG  
    # but we want it as RGB and  
    # we also need a grayscale  
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 

    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Creates the environment  
    # of the picture and shows it 
    # plt.subplot(1, 1, 1) 
    # plt.imshow(img) 
    # plt.show() 

if __name__ == "__main__":
    main()