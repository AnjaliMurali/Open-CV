import cv2
import numpy as np
import time

#print(cv2.__version__)

#Read the Video
raw_video = cv2.VideoCapture("Lesson 7/video.mp4")

#To give the video capture object some time to initialize.
time.sleep(1)

#to go through all the frames in the video 
count = 0

#to store the image of the empty background.
background = 0

"""
Loop is run 60 times to capture the first 60 frames of the video.
return_val, background = raw_video.read()
The read() function returns two values:
1. return_val: Tells us whether the frame was successfully read.
2. background: Contains the actual image/frame.
For example:
- If the frame is successfully read, return_val = True.
- If the frame cannot be read, return_val = False.
if return_val == False:
    continue
- If the frame wasn't captured, skip the current iteration and move to the next iteration.
Important: The code keeps overwriting background during these 60 iterations.
Therefore, after the loop, background contains the last successfully captured frame, not all 60 frames.f
"""
# Explanation above. The video has some seconds in the starting where the background is completely visible, Capturing that backgrund which would be used for masking later.
for i in range(60):
    return_val, background = raw_video.read()
    if return_val == False:
        continue

"""
The video frames will be flipped later.
So to ensure that the background and video frames have the same orientation - 
we need to horizontally flip (axis=1 - left becomes right and right becomes left) it. 
"""
# To join hands one hand has to be the mirror image of the other.
background = np.flip(background, axis = 1)


while(raw_video.isOpened()):
    return_val, img = raw_video.read()
    if not return_val:
        break
    count += 1
    img = np.flip(img, axis = 1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([100, 40, 40])
    upper_red = np.array([100, 255, 255])
    
    #A mask is an image that identifies which pixels satisfy a particular condition.
    #cv2.inRange() checks every pixel in the HSV image.
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    #This range covers the high end of the hue scale, where red colors can also appear.
    lower_red = np.array([155, 40, 40])
    upper_red = np.array([180, 255, 255])

    #We need 2 masks Because red appears at both ends of the HSV hue spectrum.
    #We need to combine both ranges to detect red more completely.
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    #Identifies all red areas in the current frame
    mask1 = mask1 + mask2

    # For refining the image as image is raw and blurry after processing in HSV format
    # Morphological image processsing  - It removes small white noise and isolated white pixels
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations = 2)
    #Dilation expands the white region to cover some of those missing pixels.
    mask1 = cv2.dilate(mask1, np.ones((3,3), np.uint8), iterations = 1)

    #Identifies non-red areas in the current frame
    mask2 = cv2.bitwise_not(mask1)

    # The masking happens here. You are adding 2 images together

    #Takes background where red was detected
    res1 = cv2.bitwise_and(background, background, mask = mask1)
    #Takes current image everywhere except red
    res2 = cv2.bitwise_and(img, img, mask = mask2)
    #Combines both results
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("INVISIBLE MAN", final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break


#for Hw - ask them to try to masks for blue color -
"""
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255]) 
"""