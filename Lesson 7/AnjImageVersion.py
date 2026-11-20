import cv2
import numpy as np

# Read the images
background = cv2.imread("Lesson 7/background.png")
img = cv2.imread("Lesson 7/image.png")

# Check whether images were loaded
if background is None or img is None:
    raise ValueError("Could not load images")

# Resize background to match the original image
background = cv2.resize(background, (img.shape[1], img.shape[0]))

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Detect red color (first range)
lower_red1 = np.array([0, 40, 40])
upper_red1 = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

# Detect red color (second range)
lower_red2 = np.array([170, 40, 40])
upper_red2 = np.array([179, 255, 255])
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

# Combine masks
mask = mask1 + mask2

# Clean the mask
kernel = np.ones((3, 3), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
mask = cv2.dilate(mask, kernel, iterations=1)

# Invert mask
mask_inv = cv2.bitwise_not(mask)

# Extract background and person
res1 = cv2.bitwise_and(background, background, mask=mask)
res2 = cv2.bitwise_and(img, img, mask=mask_inv)

# Combine both images
final_output = cv2.add(res1, res2)

# Display result
cv2.imshow("Invisible Effect", final_output)

cv2.waitKey(0)
cv2.destroyAllWindows()
