import cv2
import os
from PIL import Image

mean_height = 0
mean_width = 0

path = "Lesson 6/prac/images"

num_of_images = len(os.listdir(path))

for file in os.listdir(path):
    img = Image.open(os.path.join(path, file))
    width, height = img.size
    #print(width,height)
    mean_width = mean_width + width
    mean_height = mean_height + height
#print(mean_width,mean_height)

mean_width = mean_width // num_of_images
mean_height = mean_height // num_of_images

new_path = "Lesson 6/prac/resizedImages"
for file in os.listdir(path):
    img = Image.open(os.path.join(path, file))
    imgResized = img.resize((mean_width,mean_height),Image.Resampling.LANCZOS)
    imgResized = imgResized.convert('RGB')
    imgResized.save(os.path.join(new_path, file),'JPEG', quality = 95)

def videoGenerator():
    video_name = os.path.join(new_path, "MyFirstVideo.avi")
    images = []
    for img in os.listdir(new_path):
        if img.lower().endswith(('.jpg', '.jpeg', '.png')):
            images.append(img)

    frame = cv2.imread(os.path.join(new_path, images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name,0,1,(width, height))
    for image in images:
            video.write(cv2.imread(os.path.join(new_path, image)))
            cv2.destroyAllWindows()
    video.release()

videoGenerator()

