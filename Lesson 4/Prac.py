import cv2 
image = cv2.imread("Lesson 4/images/pika.png")
font = cv2.FONT_HERSHEY_COMPLEX_SMALL|cv2.FONT_ITALIC
image = cv2.putText(image,"Hello",(75,100),font,2,(255,0,0),5)
cv2.imshow("Image", image) 
cv2.waitKey(0)

import cv2
import numpy as np

# Create a white canvas (height=500, width=800)
image = np.ones((500, 800, 3), dtype=np.uint8) * 255
image = cv2.line(image,(0,0),(191,263),(0,0,255),2)
image = cv2.rectangle(image, (0,0), (191,263), (255,0,0), 9)
image = cv2.circle(image, (95,131), 10, (0,255,0), 5)
image = cv2.putText(image, 'Pika',(40,40), cv2.FONT_HERSHEY_COMPLEX_SMALL|cv2.FONT_ITALIC, 1, (0,0,0), 2,cv2.LINE_AA)

cv2.imshow("White Canvas", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#planned Hw - to draw indian flag on white canvas using all these concepts. 