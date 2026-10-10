#Refer - https://www.geeksforgeeks.org/opencv-python-tutorial/

#Concepts covered : Grayscaling, Rotation, Edge Detection and RGB <-> HSV Transformation


##### Grayscaling of an image read as colored

import cv2
 
image = cv2.imread('Lesson 3/images/pika.png')
cv2.imshow('Original Image', image)
cv2.waitKey(0)
 
# Use the cvtColor() function to grayscale the image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)

cv2.waitKey(0) 
cv2.destroyAllWindows() 

# Using averaging of pixels method to grayscale the image
# Without using the library to grayscale the image

#Read the GrayScaleUsingAveraging_Notes.md

import cv2
import numpy as np
img = cv2.imread('Lesson 3/images/pika.png')
img = img.astype(np.int32)
(row, col) = img.shape[0:2]

for i in range(row):
	for j in range(col):
		# Find the average of the BGR pixel values
		average = int(sum(img[i, j]) / 3)
		#img[i, j] = sum(img[i, j]) * 0.33
		img[i, j] = [average, average, average]


img = img.astype(np.uint8)
cv2.imshow('Grayscale Image by Averaging', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


##### Convert the image from one color frame to another
# Convert an image from RGB to HSV 

# Python program to explain cv2.cvtColor() method

"""
H — Hue → the type of color (red, green, blue, etc.)
S — Saturation → how strong/pure the color is
V — Value → how bright the color is

HSV's advantage isn't visual quality; 
it's that the color information is organized in a way that can make certain processing tasks much easier.
"""

import cv2
image = cv2.imread('Lesson 3/images/pika.png')
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV )
cv2.imshow("OriginalImage", image)
cv2.imshow("colorChanged", hsvImage)
cv2.waitKey(0)
cv2.destroyAllWindows()


##### Rotating an image
import cv2

img = cv2.imread("Lesson 3/images/pika.png")
(rows, cols) = img.shape[:2]

# getRotationMatrix2D creates a matrix needed for transformation.
# We want matrix for rotation w.r.t center to 45 degree without scaling.

#getRotationMatrix2D() creates a special matrix that 
# tells OpenCV - How should the pixels be moved to rotate the image?
#cv2.getRotationMatrix2D(center, angle, scale)
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
#cv2.warpAffine(image, transformation_matrix, output_size) performs the transformation
#Take img, apply the rotation described by M, 
# and create an output image with the same width and height.
res = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('RotatedResult', res)
cv2.imwrite('Lesson 3/images/RotatedResult.jpg', res)


##### Edge Detection in an image
import cv2
img = cv2.imread('Lesson 3/images/pika.png')
# We are using the Canny Edge Detection Algorithm here
# No need to dive deep into explanation over here
#100 is lower threshold, 200 is upper threshold - The two numbers control how sensitive the edge detection is.
edges = cv2.Canny(img, 100,200)
cv2.imshow("Edge Detection", edges)
cv2.imwrite('Lesson 3/images/result.jpg', edges)




