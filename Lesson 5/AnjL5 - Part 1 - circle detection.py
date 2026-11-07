#OpenCV's HoughCircles() function to detect circular objects in an image.

import cv2
import numpy as np

img = cv2.imread('Lesson 5/humanEyes.jpeg')

#Hough Circle Detection works with image intensity and edges rather than color information. 
# Converting the image to grayscale simplifies the processing.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Blurring helps reduce noise and small variations in pixel intensity.
#This makes circle detection more accurate because unnecessary edges and details are reduced.
gray_blurred = cv2.blur(gray, (3,3))

# Give a brief overview of what does HoughCirlces function do and What are the parameters required.
detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40)
"""
Parameter	Value	Explanation
gray_blurred	-Image	-Input grayscale, blurred image.
cv2.HOUGH_GRADIENT-	Method	-Specifies the Hough Gradient method used to detect circles.
dp-	1	-Inverse ratio of the accumulator resolution to the image resolution. A value of 1 means both resolutions are the same.
minDist	-20	-Minimum distance between the centers of detected circles, in pixels.
param1-	50-	Higher threshold for the internal Canny edge detector. The lower threshold is typically half of this value.
param2	-30	-Accumulator threshold for circle detection. Smaller values may detect more circles, including false ones.
minRadius-	1-	Minimum radius of a circle to be detected, in pixels.
maxRadius	-40-	Maximum radius of a circle to be detected, in pixels.
"""

print(detected_circles)  #function returns (x, y, radius)

if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))
    #np.around() - Rounds the detected circle values to the nearest whole number.
    #uint16 - Converts the rounded values into unsigned 16-bit integers.This is useful because OpenCV's drawing functions require integer pixel coordinates and radius values.
    for pt in detected_circles[0, :] :
        a, b, r = pt[0], pt[1], pt[2]
        cv2.circle(img, (a,b), r, (0, 255, 0), 2)
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
        cv2.imshow("Detected Circles", img)
        cv2.waitKey(0)

cv2.destroyAllWindows()