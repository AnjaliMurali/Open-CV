import cv2 
image = cv2.imread("Lesson 4/images/pika.png")
image = cv2.line(image,(0,0),(191,263),(0,0,255),2)
image = cv2.rectangle(image, (0,0), (191,263), (255,0,0), 9)
image = cv2.circle(image, (95,131), 10, (0,255,0), 5)
image = cv2.putText(image, 'Pika',(40,40), cv2.FONT_HERSHEY_COMPLEX_SMALL|cv2.FONT_ITALIC, 1, (0,0,0), 2,cv2.LINE_AA)
cv2.imshow("Image", image) 
cv2.waitKey(0)
cv2.destroyAllWindows()