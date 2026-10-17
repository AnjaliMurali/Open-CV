import cv2
import numpy as np

# Create a blank image (white background)
img = cv2.imread("Lesson 4/images/pika.png")

# Draw the base of the hut (rectangle for walls)
cv2.rectangle(img, (10, 80), (180, 250), (153, 102, 51), 2)  # Brown wall

# Draw the roof (triangle)
roof_pts = np.array([[10, 80], [85,0], [180,80]], np.int32)
cv2.fillPoly(img, [roof_pts], (102, 51, 0))  # Dark brown roof

#not complete - need to fix the coordinates for the below shapes. 
# Draw door
cv2.rectangle(img, (270, 360), (330, 450), (0, 0, 0), -1)  # Black door

# Optional: draw windows
cv2.rectangle(img, (220, 340), (250, 370), (255, 255, 0), -1)  # Left window
cv2.rectangle(img, (350, 340), (380, 370), (255, 255, 0), -1)  # Right window

# Optional: door knob
cv2.circle(img, (325, 405), 5, (255, 255, 255), -1)

# Show the image
cv2.imshow("Hut", img)
cv2.waitKey(0)
cv2.destroyAllWindows()