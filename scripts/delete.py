# call to delete all images in results folder with a certain name_addition and location
# python3 timelapse.py [location] [name_addition]

print("Loading libraries...")
import sys
import os
from dotenv import load_dotenv

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

print("Loading files...")
images = [img for img in os.listdir(img_folder) if img.endswith(".jpg") and location in img and name_addition in img]


print("Writing video...")
for image in images:
    os.remove(os.path.join(img_folder, image))
