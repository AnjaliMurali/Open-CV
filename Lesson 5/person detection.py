import cv2
import numpy as np
image = cv2.imread('Lesson 5/people1.jpg', 0)

# Give a basic overview of the SimpleBlobDetecter function, Why it is used and What are the parameters required.

# Set our filtering parameters Initialize parameter settiing using cv2.SimpleBlobDetector
params = cv2.SimpleBlobDetector_Params()

# Set Area filtering parameters
params = cv2.SimpleBlobDetector_Params()

# Area filtering
params.filterByArea = True
params.minArea = 100
params.maxArea = 10000

# Circularity filtering
params.filterByCircularity = True
params.minCircularity = 0.1

# Convexity filtering
params.filterByConvexity = True
params.minConvexity = 0.1

# Inertia filtering
params.filterByInertia = True
params.minInertiaRatio = 0.1


# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)
	
# Detect blobs
#A keypoint contains information about the detected blob.
keypoints = detector.detect(image)

print (keypoints)

# Draw blobs on our image as red circles
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS - the circles reflect their detected sizes.
#cv2.DRAW_MATCHES_FLAGS_DEFAULT - the keypoints are drawn using simpler markers.

number_of_blobs = len(keypoints)
text = "Number of Circular Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 100, 255), 2)

# Show blobs
cv2.imshow("Filtering Circular Blobs Only", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()