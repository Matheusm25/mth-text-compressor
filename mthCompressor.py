# Program made by Matheus Marques Lima

# Split the file name to get the extension, if it is mth i'll decompress, otherwise i'll compress

import sys
import compressor
import decompressor

file = sys.argv[1]
try:
    extension = file.split('.')[1]
except IndexError:
    print('File without extension! please enter the complete file name.')
    exit(0)

if extension == 'mth':
    decompressor.decompress(file)
else:
    compressor.compress(file)
