######Concepts convered: 
#Operations on Image, Erosion of Image, Blurring an Image, Image Resizing, Image Bordering

###### NOTE: make sure that the 2 images are of same size

import cv2 

image1 = cv2.imread("Lesson 2/images/dump truck.jpg") 
image2 = cv2.imread("Lesson 2/images/excavator.jpg")

# 0.5 and 0.4 are weights to be multiplied for each pixel, 0 is gamma_value (measurement of light)
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
  
cv2.imshow('Weighted Image', weightedSum)

cv2.waitKey(0) 
cv2.destroyAllWindows()

"""
cv2.addWeighted() is mainly used to blend two images by controlling 
the contribution (weight) of each image. 

Weight in cv2.addWeighted()

cv2.addWeighted(image1, weight1, image2, weight2, gamma)
Weight determines how much each image contributes to the final image.
Larger weight → greater influence of that image.
Weight = 0 → image has no contribution.
Weight = 1 → full pixel values are used.
Weights do not have to add up to 1.
Gamma (brightness adjustment)

Formula:

Output = (image1 × weight1) + (image2 × weight2) + gamma

Examples:

(0.5, 0.5) → equal blend
(0.8, 0.2) → image1 has greater influence
(1, 0)     → only image1
(0, 1)     → only image2
(0, 0)     → black image if gamma = 0
Weight = 2     → image contributes twice (can cause very bright pixels

⚠️ Note: Large weights can make pixel values exceed 255, 
causing bright/white areas due to pixel-value clipping.
(When total px value (output) > 255, it clips to 255 making it white color.)

Gamma (brightness adjustment)
Gamma is added to every pixel after the weighted sum. 
A small gamma such as 10 produces a very dark gray image, which may appear black.
0   → black
10  → very dark gray
128 → medium gray
255 → white
"""

# Subtraction of images

sub = cv2.subtract(image1, image2) 
cv2.imshow('Subtracted Image', sub)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
subtracts the pixel values of image2 from image1.
if image 2 has higher value, example 
image2 = 200
image1 = 50
output : 50-200 = -150. Opencv cannot handle negative values, so output will be clipped at 0. 
It is useful for detecting differences or changes between images.
"""

##### Image Resizing
img = cv2.imread("Lesson 2/images/dump truck.jpg",1)
cv2.imshow("Original Image", image1)

# The order of dimensions is (WIDTH, HEIGHT)
resized = cv2.resize(img, (500, 250))
cv2.imshow("reducedImage", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()

##### Erosion of an image, corners are trimmed in erosion
import cv2
import numpy as np
  
image = cv2.imread("Lesson 2/images/dump truck.jpg", 1) 
cv2.imshow("Original Image", image) 
# kernel is used for erosion as an input
kernel = np.ones((5, 5), np.uint8)

image = cv2.erode(image, kernel) 
cv2.imshow("Eroded Image", image)

cv2.waitKey(0) 
cv2.destroyAllWindows()

"""
Erosion is a morphological image-processing operation that 
shrinks the foreground/bright regions of an image by removing
pixels around their boundaries.

Kernel → small matrix/window used to process the image.
(5,5) → kernel size.
Larger kernel → generally stronger erosion.
Erosion → shrinks foreground objects and can remove small bright details/noise.
"""


##### Bluring of an image
"""
Image blurring is used to reduce sharpness and make image appear smoother. 
This is done by applying filters also called low-pass filters 
that reduce high-frequency noise and smooth finer details. 
Blurring is used for tasks like noise reduction, edge smoothing or creating artistic effects.
"""
import cv2

image = cv2.imread("Lesson 2/images/dump truck.jpg")

cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Gaussian Blur - used mostly in machine learning preprocessing steps
Gaussian = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('Gaussian Blurring', Gaussian)
cv2.waitKey(0)

"""
Pixels closer to the center have greater influence, while pixels farther away have less influence.
The weights follow a Gaussian (bell-shaped) distribution and hence the name Gaussian Blurring.
(7, 7) → kernel size
0 → OpenCV automatically calculates sigmaX (The Gaussian spread)
Larger kernel → generally stronger blur
Used to reduce noise and smooth the image, often before further image processing.
"""

# Median Blur - used in digital processing preserves edges but removes noise
median = cv2.medianBlur(image, 5)
cv2.imshow('Median Blurring', median) 
cv2.waitKey(0)

"""
Median Blur replaces each pixel with the median value of its neighboring pixels. 
It is particularly effective for removing salt-and-pepper noise while preserving edges.
image → input image
5 → 5 × 5 neighborhood
Larger kernel → generally stronger smoothing
Kernel size should be a positive odd number such as 3, 5, 7, etc.
"""


# Bilateral Blur - only sharp edges are preserved here
bilateral = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow('Bilateral Blurring', bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Bilateral filtering smooths an image while preserving strong edges. 
It considers both the spatial distance between pixels and their color/intensity differences.

bilateral = cv2.bilateralFilter(image, 9, 75, 75)
image → input image
9 → neighborhood diameter
75 → sigmaColor
75 → sigmaSpace
Useful for noise reduction while preserving edges.
Generally more computationally expensive than Gaussian or median filtering.
"""


##### Bordering an image
#cv2.copyMakeBorder(image, top, bottom, left, right, borderType, colorValue)

# SOLID Border around an image
import cv2

img = cv2.imread("Lesson 2/images/excavator.jpg")
#borderedImage = cv2.copyMakeBorder(img, 10, 100, 20, 10, cv2.BORDER_CONSTANT, value = (255,0,0)) blue border because BGR
borderedImage = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = 1) #black border coz BGR all 3 colors have value 1
#cv2.namedWindow("Bordered Image", cv2.WINDOW_NORMAL)
#cv2.resizeWindow("Bordered Image", 800, 600)
# use the above 2 lines if your output window is bigger than screen and you want to see the bottom border
cv2.imshow("Bordered Image", borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Reflective Border around an image
import cv2
img = cv2.imread("Lesson 2/images/excavator.jpg")
#Important - For cv2.BORDER_REFLECT, you do not need to provide value because OpenCV 
#            creates the border by reflecting the image pixels.
borderedImage = cv2.copyMakeBorder(img, 10, 10, 100, 10, cv2.BORDER_REFLECT)
#cv2.namedWindow("Bordered Image", cv2.WINDOW_NORMAL)
#cv2.resizeWindow("Bordered Image", 800, 600)
cv2.imshow("Bordered Image", borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()