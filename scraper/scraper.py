from PIL import Image

import pytesseract
import os
import zipfile
import shutil




def gettextfromworddocimages(wordfilepath, targetdir):
    document = zipfile.ZipFile(wordfilepath)
    filelist = document.namelist()
    images = []
    imagenames = [x for x in filelist if x.endswith('.jpg') or x.endswith('.png') or x.endswith('.gif')]
    for i in imagenames:
        images.append(document.extract(i))
    count = 0
    try:
        os.mkdir(targetdir + "/" + os.path.basename(wordfilepath) + "/")
    except:
        print("Directory already exists, shouldn't interfere")
    for file in images:
        convertedpyfile = open(targetdir + "/" + os.path.basename(wordfilepath) + "/" + "extractedtext" + str(count) + ".py", "w+")
        convertedpyfile.write(pytesseract.image_to_string(Image.open(file).convert('LA')))
        count += 1

def convertentiredirectory(source, target):
    allfilesindir = os.listdir(source)
    print(allfilesindir)
    for file in allfilesindir:
        print(file)
        if file.endswith(".docx"):
            gettextfromworddocimages(source + "/" + file, target)


##gettextfromworddocimages("HOP05 – Organizing Files and Debugging.docx", r"C:/Users/cmatza/Documents/extracted")
sourcedir = input("Please enter the *full* filepath for the source directory of your word documents\n>>>")
targetdir = input("Please enter the *full* filepath of the target output directory\n>>>")
print("Output will be in target/originalfilename/extractedtext(number) where number is the sequential number in which the file was processed")
convertentiredirectory(sourcedir, targetdir)

