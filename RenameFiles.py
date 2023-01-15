# Rename files in block.

import os

# this variable contains a paste of directory files to be renamed.
foldersToRename = ''' 
IMG_3233.jpeg
IMG_3232.jpeg
IMG_3231.jpeg
IMG_3230.jpeg
IMG_3229.jpeg
IMG_3228.jpeg
'''


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

            if os.path.exists(pictureFolder) == False:
                os.mkdir(pictureFolder)

            if os.path.exists(audioFolder) == False:
                os.mkdir(audioFolder)

            if os.path.exists(videoFolder) == False:
                os.mkdir(videoFolder)

            if os.path.exists(compressedFolder) == False:
                os.mkdir(compressedFolder)

            if os.path.exists(othersFolder) == False:
                os.mkdir(othersFolder)

            # extensions should be configured in mover.json: "fileExtensions"

            # compress image file and move them to picture folder.
            if extension in extensions['picturesExtensions']:
                picture = Image.open(downloadFolder + filename)
                picture.save(downloadFolder + filename, optimize=True)
                os.replace((downloadFolder + filename),
                           pictureFolder + filename)

            # compress image file and move them to picture folder.
            elif extension in extensions['audioExtensions']:
                os.replace(downloadFolder + filename, audioFolder + filename)

            # compress image file and move them to picture folder.
            elif extension in extensions['videoExtensions']:
                os.replace(downloadFolder + filename, videoFolder + filename)

            # rename compressed files to compressed folderr.
            elif extension in extensions['compressedExtensions']:
                os.replace(downloadFolder + filename,
                           compressedFolder + filename)

            elif (filename in afiles):
                os.replace(downloadFolder + filename, othersFolder + filename)

            counter += 1
        # script log.

        print(f'{counter} file(s) were(was) moved  to folders')
    except (NameError):
        print("Somenthing went wrong: " + NameError)
