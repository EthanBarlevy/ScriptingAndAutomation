import glob
import os, shutil
from PIL import Image

if os.path.exists("./new_images"):
    shutil.rmtree("./new_images")

os.mkdir("./new_images")

box = (25, 0, 225, 200)

def ProcessImages(source, destination):
    with Image.open(source) as img:
        img = img.crop(box)
        #img.paste(region, box)
        img = img.rotate(270)
        img.thumbnail((75, 75))
        img = img.convert("L")
        img.save(destination, "PNG", optimize=True, quality=80)

counter = 0

paths = glob.glob("./images/*.jpg")
for path in paths:
    counter += 1
    ProcessImages(path, "./new_images/pic" + str(counter).zfill(4) + '.png')