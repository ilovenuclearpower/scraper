from PIL import Image

import pytesseract
import os
import zipfile
import shutil




def get_text_from_images(word_file_path, target_dir):
    ##Opens the target file. We can treat a .docx document as a zip archive directly.
    document = zipfile.ZipFile(word_file_path)
    ##Gets a list of the all members in the word document
    file_list = document.namelist()
    images = []
    ##Returns a list containing the name of all files with image file extensions
    image_names = [x for x in file_list if x.endswith('.jpg') or x.endswith('.png') or x.endswith('.gif')]
    ##Uses the list to extract every image file into the list of images
    for i in image_names:
        images.append(document.extract(i))
    
    #Counter to append to all of our filenames so we don't overwrite outselves
    count = 0

    ##Makes destination directory
    try:
        os.mkdir(target_dir + "/" + os.path.basename(word_file_path) + "/")
    except:
        print("Directory already exists, shouldn't interfere")

    ##Opens a desired file and writes the output of the OCR conversion to the file, then increments count
    for file in images:
        converted_py_file = open(target_dir + "/" + os.path.basename(word_file_path) + "/" + "extractedtext" + str(count) + ".py", "w+")

        ##Uses pytesseract on the image file we grabbed, converts to grayscale using Pillow, then runs the pytesseract ocr image-to-string conversion
        converted_py_file.write(pytesseract.image_to_string(Image.open(file).convert('LA')))
        converted_py_file.close()
        count += 1


##Grabs every file in a given directory then calls get_text_from_images

def convert_entire_directory(source, target):
    all_files_in_dir = os.listdir(source)
    print(all_files_in_dir)
    for file in all_files_in_dir:
        print(file)
        if file.endswith(".docx"):
            get_text_from_images(source + "/" + file, target)


source_dir = input("Please enter the *full* filepath for the source directory of your word documents\n>>>")
target_dir = input("Please enter the *full* filepath of the target output directory\n>>>")
print("Output will be in target/originalfilename/extractedtext(number) where number is the sequential number in which the file was processed")
convert_entire_directory(source_dir, target_dir)

