# call to make a timelapse from images in results folder
# python3 timelapse.py [location] [name_addition] [fps] [video_name]

print("Loading libraries...")
import sys
import os
from dotenv import load_dotenv
import cv2
import time

print("Loading .env file...")
load_dotenv()
img_folder = os.getenv("REPOLOC") + "/results"

print("Loading arguments...")
location = "Hamburg-SW"
if len(sys.argv) > 1:
    location = sys.argv[1]

name_addition = ""
if len(sys.argv) > 2:
    name_addition = sys.argv[2] + "_"

fps = 18
if len(sys.argv) > 3:
    fps = sys.argv[3]

video_name = location + '_' + name_addition + str(time.time()).replace(".", "-") + ".mp4"
if len(sys.argv) > 4:
    video_name = sys.argv[4] + ".mp4"

video_name = img_folder + '/' + video_name

print("Loading images...")
images = [img for img in os.listdir(img_folder) if img.endswith(".jpg") and location in img and name_addition in img]
frame = cv2.imread(os.path.join(img_folder, images[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(video_name, fourcc, fps, (width,height))

print("Sorting images...")
images.sort()

print("Writing video...")
for image in images:
    video.write(cv2.imread(os.path.join(img_folder, image)))

cv2.destroyAllWindows()
video.release()