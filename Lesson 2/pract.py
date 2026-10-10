import cv2

img = cv2.imread("Lesson 2/images/dump truck.jpg")
resized = cv2.resize(img, (250, 250))
#borderedImage = cv2.copyMakeBorder(img, 10, 100, 20, 10, cv2.BORDER_CONSTANT, value = (255,0,0)) blue border because BGR
borderedImage = cv2.copyMakeBorder(resized, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value = 1) #black border coz BGR all 3 colors have value 1
#cv2.namedWindow("Bordered Image", cv2.WINDOW_NORMAL)
#cv2.resizeWindow("Bordered Image", 800, 600)
# use the above 2 lines if your output window is bigger than screen and you want to see the bottom border
cv2.imshow("Bordered Image", borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Reflective Border around an image
import cv2
img = cv2.imread("Lesson 2/images/dump truck.jpg")
resized = cv2.resize(img, (250, 250))
#Important - For cv2.BORDER_REFLECT, you do not need to provide value because OpenCV 
#            creates the border by reflecting the image pixels.
borderedImage = cv2.copyMakeBorder(resized, 50, 50, 50, 50, cv2.BORDER_REFLECT)
#cv2.namedWindow("Bordered Image", cv2.WINDOW_NORMAL)
#cv2.resizeWindow("Bordered Image", 800, 600)
cv2.imshow("Reflective Border", borderedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()