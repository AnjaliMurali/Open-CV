####save an image using openCV after some change

import cv2
# OS library to handle the directory functionalities
import os

# change the path to where you wish to save the image
saved_directory = "Lesson 1/images"

img = cv2.imread("Lesson 1/images/pika.png", 0)
cv2.imshow("Pikachu in Black and White", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Change the current execution directory to 
os.chdir(saved_directory)

# write image to this directory
cv2.imwrite("pikaBlackWhite.png", img)
print("Successfully Saved")