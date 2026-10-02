import cv2

# 1. Read the image
image = cv2.imread("Lesson 1/images/landscape.png")

# Check that the image was loaded
if image is None:
    print("Could not read landscape.png")
    exit()

# 2. Convert to grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

"""
H — Hue → the type of color (red, green, blue, etc.)
S — Saturation → how strong/pure the color is
V — Value → how bright the color is

HSV's advantage isn't visual quality; 
it's that the color information is organized in a way that can make certain processing tasks much easier.
"""

#Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 3. Save the grayscale image
cv2.imwrite("landscape_gray.jpg", gray)

# 4. Save the HSV image
cv2.imwrite("landscape_hsv.jpg", hsv)

# 5. Display all three images in separate windows
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.imshow("HSV", hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()

