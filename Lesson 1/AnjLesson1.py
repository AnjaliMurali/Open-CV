import cv2
import os #For change directory

img = cv2.imread("Lesson 1/images/star fish.jpeg",cv2.IMREAD_COLOR)
#img_resized = cv2.resize(img, (new_width, new_height))
img_resized = cv2.resize(img, (200, 270))
cv2.imshow("Star Fish", img_resized)
cv2.waitKey(0) #pauses the program until key pressed
cv2.destroyAllWindows()  # closes all open cv windows. This is important in bigger codes. 

"""
# There are 3 parameters to read an image - (visibly seen in PNG files)
#cv2.IMREAD_COLOR (1) => Specify to load the image in color
#cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
#cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged including the alpha(transparency)if present
"""

####### Read and display an image in grayscale 
img = cv2.imread("Lesson 1/images/star fish.jpeg",0)
#img_resized = cv2.resize(img, (new_width, new_height))
img_resized = cv2.resize(img, (200, 270))
cv2.imshow("Star Fish", img_resized)
cv2.waitKey(0)

### save the image

cv2.imwrite("StarFishBlackWhite.jpeg", img_resized)
print("Successfully Saved")


### change the path to where you wish to save the image
saved_directory = "Lesson 1/images"
os.chdir(saved_directory)
cv2.imwrite("StarFishBlackWhite.jpeg", img_resized)
print("Successfully Saved")


##############Activity 2 ##########


##### Print an image in different color formats
# OpenCV default color format is RGB

image = cv2.imread("Lesson 1/images/pika.png",1)
cv2.imshow("original", image)
cv2.waitKey(0)

# Split the above image in red, blue and green different saturations
# OpenCV uses BGR, not RGB.
B, G, R = cv2.split(image)

"""
B contains the amount (intensity) of Blue in each pixel. 
Depending on the Blue intensity, it is displayed as a shade of gray.
For example:
Blue intensity     Grayscale display
-------------------------------------
0                  Black
50                 Dark gray
128                Gray
200                Light gray
255                White
"""
cv2.imshow("Blue Channel Image", B)
cv2.waitKey(0)

cv2.imshow("Green Channel Image", G)
cv2.waitKey(0)
  
cv2.imshow("Red Channel Image", R)
cv2.waitKey(0)

cv2.destroyAllWindows() 