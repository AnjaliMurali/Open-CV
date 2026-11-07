import cv2
import numpy as np

# Read image in grayscale for blob detection
imageOG = cv2.imread('Lesson 5/square blob.jpg', 0)
image = cv2.imread('Lesson 5/square blob.jpg', 0)

if image is None:
    print("Image not found. Check the file path.")
    exit()

# Initialize blob detector parameters
params = cv2.SimpleBlobDetector_Params()

# Area filter
params.filterByArea = True
params.minArea = 500
params.maxArea = 20000

# Circularity filter
params.filterByCircularity = True
params.minCircularity = 0.7
params.maxCircularity = 0.8

# Convexity filter
params.filterByConvexity = True
params.minConvexity = 0.9

# Inertia filter
params.filterByInertia = True
params.minInertiaRatio = 0.7

# Threshold settings
params.minThreshold = 10
params.maxThreshold = 220
params.thresholdStep = 10

# Minimum distance between blobs
params.minDistBetweenBlobs = 2

# Create detector
detector = cv2.SimpleBlobDetector_create(params)

# Detect blobs
keypoints = detector.detect(image)

print("Number of detected blobs:", len(keypoints))

# Convert grayscale image to BGR for coloured drawing
blobs = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# Draw square outlines around detected keypoints
for kp in keypoints:

    x = int(kp.pt[0])
    y = int(kp.pt[1])

    size = int(kp.size / 2)

    cv2.rectangle(
        blobs,
        (x - size, y - size),
        (x + size, y + size),
        (0, 0, 255),
        2
    )

cv2.imshow("Blobs", imageOG)
cv2.imshow("Detected Square Blobs", blobs)

cv2.waitKey(0)
cv2.destroyAllWindows()