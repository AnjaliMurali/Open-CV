##### Read and display an image in grayscale 

import cv2

img = cv2.imread("Lesson 1/images/pika.png", 0)
cv2.imshow("Pikachu in Grayscale", img)
cv2.waitKey(0)
cv2.destroyAllWindows()