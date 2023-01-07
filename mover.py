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
videoFolder = params['videoFolder']
extensions = params['filesExtensions']

if __name__ == "__main__":


    counter = 0
    for filename in os.listdir(downloadFolder):
        name, extension = os.path.splitext(downloadFolder + filename)

        # validating folder
        if os.path.exists(pictureFolder) == False: os.mkdir(pictureFolder)

        if os.path.exists(audioFolder) == False: os.mkdir(audioFolder)

        if os.path.exists(videoFolder) == False: os.mkdir(videoFolder)

        if os.path.exists(compressedFolder) == False: os.mkdir(compressedFolder)

        if os.path.exists(othersFolder) == False: os.mkdir(othersFolder)
        
        if  extension in extensions['picturesExtensions']: # compress image file and move them to picture folder.
            picture = Image.open(downloadFolder + filename)
            picture.save(pictureFolder + "compressed_" + filename, optimize=True)
            os.remove(downloadFolder + filename)
            counter += 1
        elif extension in extensions['audioExtensions']: # compress image file and move them to picture folder.
                os.rename(downloadFolder + filename, audioFolder + filename)
                counter += 1
        elif extension in extensions['videoExtensions']: # compress image file and move them to picture folder.
            os.rename(downloadFolder + filename, videoFolder + filename)
            counter += 1
        elif extension in extensions['compressedExtensions']: # rename compressed files to compressed folderr.
            os.rename(downloadFolder + filename, compressedFolder + filename)
            counter += 1
        else:
            os.rename(downloadFolder + filename, othersFolder + filename)
            counter += 1



    print(f'there were compressed and moved {counter} file(s)')


        

