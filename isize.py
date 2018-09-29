# coding: utf-8

import sys
import os.path
from PIL import Image

if len(sys.argv) < 3:
    print('Usage: python3 isize.py [image filename] [new size (e.g. 256)] ([new image filename (e.g. new_img.png)])')
    sys.exit()

img = Image.open(sys.argv[1], 'r')
new_size = int(sys.argv[2])
new_size = (new_size, new_size)
img.thumbnail(new_size)

if len(sys.argv) == 4:
    new_name = sys.argv[3]
else:
    new_name = '%s-resize.png' % os.path.splitext(sys.argv[1])[0]
img.save(new_name)
