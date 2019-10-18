from PIL import Image

import pytesseract
import os
import zipfile
import shutil




def gettextfromworddocimages(wordfilepath, targetdir):
    ##Opens the target file. We can treat a .docx document as a zip archive directly.
    document = zipfile.ZipFile(wordfilepath)
    ##Gets a list of the all members in the word document
    filelist = document.namelist()
    images = []
    ##Returns a list containing the name of all files with image file extensions
    imagenames = [x for x in filelist if x.endswith('.jpg') or x.endswith('.png') or x.endswith('.gif')]
    ##Uses the list to extract every image file into the list of images
    for i in imagenames:
        images.append(document.extract(i))
    
    #Counter to append to all of our filenames so we don't overwrite outselves
    count = 0

    ##Makes destination directory
    try:
        os.mkdir(targetdir + "/" + os.path.basename(wordfilepath) + "/")
    except:
        print("Directory already exists, shouldn't interfere")

    ##Opens a desired file and writes the output of the OCR conversion to the file, then increments count
    for file in images:
        convertedpyfile = open(targetdir + "/" + os.path.basename(wordfilepath) + "/" + "extractedtext" + str(count) + ".py", "w+")

        ##Uses pytesseract on every image file we grabbed, converts to grayscale using Pillow, then runs the pytesseract ocr image-to-string conversion
        convertedpyfile.write(pytesseract.image_to_string(Image.open(file).convert('LA')))
        count += 1


##Grabs every file in a given directory then calls gettextfromworddocimages

def convertentiredirectory(source, target):
    allfilesindir = os.listdir(source)
    print(allfilesindir)
    for file in allfilesindir:
        print(file)
        if file.endswith(".docx"):
            gettextfromworddocimages(source + "/" + file, target)


sourcedir = input("Please enter the *full* filepath for the source directory of your word documents\n>>>")
targetdir = input("Please enter the *full* filepath of the target output directory\n>>>")
print("Output will be in target/originalfilename/extractedtext(number) where number is the sequential number in which the file was processed")
convertentiredirectory(sourcedir, targetdir)

