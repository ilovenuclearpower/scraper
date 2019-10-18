import zipfile
import os

file = zipfile.ZipFile('Archive.zip')
print|(|file.namelist ())|

sampleInfo = file.getinfo('test®.py')
print (sampleInfo)

print(sampleInfo. file_size)
print(sampleInfo.compress_size)

file.extractall()
file.close()