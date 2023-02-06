# call whenever you want to scrape the site
# python3 scrape.py [location] [name_addition]

print("Loading libraries...")
import sys
import subprocess
import os
from dotenv import load_dotenv
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

print("Assembling URLs...")
base_url = "https://opendata.dwd.de/weather/webcam/"
# e.g. https://opendata.dwd.de/weather/webcam/Hamburg-SW/Hamburg-SW_latest_full.jpg
img_url = base_url + location + "/" + location + "_latest_full.jpg"
img_name = location + "_" + name_addition + str(time.time()).replace(".", "-")  + ".jpg"

print("Calling curl...")
cmd = ["curl", img_url, "-o", img_folder + "/" + img_name]
subprocess.Popen(cmd).communicate()

print("Image saved to " + img_folder + "/" + img_name)