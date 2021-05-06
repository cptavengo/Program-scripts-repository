#!/usr/bin/env python3

import os
from pathlib import Path
from PIL import Image

location = input("Where are the photos located? ")
location = str(location)

if Path("/opt/icons").exists() == False:
    os.chdir("/")
    os.mkdir("opt")
    os.chdir("/opt")
    os.mkdir("icons")

new_icons_dir = "/opt/icons/"
file_location = Path("/home/cptavengo/").joinpath(location)
os.chdir(file_location)
cwd = os.getcwd()

def image_corrector():
    images = os.listdir(cwd)
    for image in images:
        if image == ".DS_Store":
            continue
        else:
            im = Image.open(image)
            im.rotate(90).resize((128, 128)).convert("RGB").save(new_icons_dir + image + ".jpg")

image_corrector()
