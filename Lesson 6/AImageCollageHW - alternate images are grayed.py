# Refer - https://www.geeksforgeeks.org/python-create-video-using-multiple-images-using-opencv/

#### Create a Video Collage (Video created out of images)

import os
import cv2
#pip install Pillow   #run the command prompt to install the Pillow package
from PIL import Image # Pillow - Image Processing Library Python Imaging Library

# Change the directory as per own folder path where the images are located
os.chdir('C:/Users/ajcha/OneDrive/Desktop/JetLearn/Moodle/OpenCV/Lesson 6/images')
path = "C:/Users/ajcha/OneDrive/Desktop/JetLearn/Moodle/OpenCV/Lesson 6/images"

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir('.')) # 7

for file in os.listdir('.'):
    img = Image.open(os.path.join(path, file))
    width, height = img.size
    mean_width = mean_width + width
    mean_height = mean_height + height


mean_width = mean_width // num_of_images
mean_height = mean_height // num_of_images

print(mean_width)
print(mean_height)

for file in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        img = Image.open(os.path.join(path, file))
        width, height = img.size
        print(width, height)

        #imgResized = img.resize((mean_width, mean_height), Image.ANTIALIAS)   #because ANTIALIAS has been deprecated from Pillow
        imgResized = img.resize((mean_width, mean_height), Image.Resampling.LANCZOS)
        imgResized.save(file, 'JPEG', quality = 95)
        print(img.filename.split('\\')[-1], " is resized")
    

        

def videoGenerator():
    video_name = "MyFirstVideo.avi"

    os.chdir('C:/Users/ajcha/OneDrive/Desktop/JetLearn/Moodle/OpenCV/Lesson 6/images')

    images = []
    for img in os.listdir('.'):
        if img.endswith('.jpg') or img.endswith('.jpeg') or img.endswith('.png'):
            images.append(img)

    print(images)

    frame = cv2.imread(os.path.join(".", images[0]))
    height, width, layers = frame.shape

    # Create a video writer object
    video = cv2.VideoWriter(video_name, 0, 1, (width, height))
    num=1
    for image in images:
        img_path = os.path.join(".", image)

        if num%2==0:
            gray_img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)  # read in grayscale
            gray_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)  # convert grayscale to BGR to match video format
            video.write(gray_img)
        else:
            color_img = cv2.imread(img_path)
            video.write(color_img)
        num+=1
    cv2.destroyAllWindows()
    video.release()

videoGenerator()
