#Scraper - An OCR Word document converter!

This program does a simple OCR extraction of ALL text from ALL images in a given word document, and outputs them as .py files. Support for roll-your-own target extensions may be added later, but it shouldn't be too hard to add it yourself if you so desire.

##Requirements:
Testing done on Python 3.8.X
pytesseract 0.3.0
Pillow 6.2.0

Recommend running:
    pip install pytesseract

Additionally you will need to have a functional copy of Tesseract-OCR installed in your computer, and in your PATH, for Windows:
    https://github.com/UB-Mannheim/tesseract/wiki
For *nix/MacOS:
    https://github.com/tesseract-ocr/tesseract

##Usage
    py scraper.py
    python scraper.py
When you run the tool, it will ask you for a full path of the sources of your doc files,
and a full path of the destination. There is no support for windows-style filepath, so please convert your filepaths to POSIX filepaths if you're on windows. (Replacing backslashes with forward slashes)
