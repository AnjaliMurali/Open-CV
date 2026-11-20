import cv2
import numpy as np
import time

# Load the video
raw_video = cv2.VideoCapture("Lesson 7/video.mp4")  # Replace with your path

# Get frame properties for output video
frame_width = int(raw_video.get(3))
frame_height = int(raw_video.get(4))
fps = int(raw_video.get(cv2.CAP_PROP_FPS))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter('output_green.avi', fourcc, fps, (frame_width, frame_height))

time.sleep(1)

while raw_video.isOpened():
    ret, frame = raw_video.read()
    if not ret:
        break

    # Flip frame (optional, based on your use-case)
    frame = np.flip(frame, axis=1)

    # Convert to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define red color ranges in HSV
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    red_mask = mask1 + mask2

    # Create green image
    green_img = np.zeros_like(frame)
    green_img[:] = [0, 255, 0]

    # Apply masks
    green_part = cv2.bitwise_and(green_img, green_img, mask=red_mask)
    rest = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(red_mask))
    final_output = cv2.add(rest, green_part)

    # Show and save the output
    cv2.imshow("Red to Green", final_output)
    video.write(final_output)

    if cv2.waitKey(10) == 27:  # ESC key to exit
        break

# Release resources
raw_video.release()
video.release()
cv2.destroyAllWindows()