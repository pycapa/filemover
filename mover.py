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

    afiles = []
    afolders = []

    with os.scandir(downloadFolder) as folders:
        for folder in folders:
            if folder.is_dir():
                afolders.append(folder.name)
            else:
                afiles.append(folder.name)

    counter = 0

    try:
        for filename in os.listdir(downloadFolder):
            name, extension = os.path.splitext(downloadFolder + filename)

            # folders validation: if folder doesn't exits the it is created.

            if os.path.exists(pictureFolder) == False: os.mkdir(pictureFolder)

            if os.path.exists(audioFolder) == False: os.mkdir(audioFolder)

            if os.path.exists(videoFolder) == False: os.mkdir(videoFolder)

            if os.path.exists(compressedFolder) == False: os.mkdir(compressedFolder)
            
            if os.path.exists(othersFolder) == False: os.mkdir(othersFolder)


            # extensions should be configured in mover.json: "fileExtensions"

            if  extension in extensions['picturesExtensions']: # compress image file and move them to picture folder.
                picture = Image.open(downloadFolder + filename)
                picture.save(downloadFolder + filename, optimize=True)
                os.replace((downloadFolder + filename), pictureFolder + filename)

            elif extension in extensions['audioExtensions']: # compress image file and move them to picture folder.
                os.replace(downloadFolder + filename, audioFolder + filename)

            elif extension in extensions['videoExtensions']: # compress image file and move them to picture folder.
                os.replace(downloadFolder + filename, videoFolder + filename)

            elif extension in extensions['compressedExtensions']:  #rename compressed files to compressed folderr.
                os.replace(downloadFolder + filename, compressedFolder + filename)

            elif (filename in afiles):
                os.replace(downloadFolder + filename, othersFolder + filename)

            counter += 1
        # script log.

        print(f'{counter} file(s) were(was) moved  to folders')
    except (NameError):
        print("Somenthing went wrong: " + NameError)



            

