# Organize download folder.
# This script organize the download folder, creating subfolders for its movmnent to a user specific folder.
# The files to be move are:
# Images files, compressed files like zip or dmg, mp3, etc. (image files it'll be compressed before move)

import os, json
from PIL import Image

# we load the json file config.

json_file = open('mover.json', 'r')
params = json.load(fp=json_file)

downloadFolder = params['downloadFolder']
pictureFolder = params['picturesFolder']
audioFolder = params['audioFolder']
compressedFolder = params['compressedFolder']
othersFolder = params['others']

print(audioFolder)