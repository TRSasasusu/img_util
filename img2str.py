# coding: utf-8

import sys
import os
from PIL import Image
import numpy as np

img = Image.open(sys.argv[1])
data = np.array(img, dtype=np.int32)

with open(sys.argv[2], 'r') as f:
    relations = {line.split(':')[0]: line.split(':')[1] for line in f.read().split('\n') if line != ''}

text = ''
for row in data:
    for cell in row:
        text += relations['{},{},{}'.format(cell[0], cell[1], cell[2])]
    text += '\n'

if len(sys.argv) == 4:
    result_filename = sys.argv[3]
else:
    result_filename = '{}.txt'.format(os.path.splitext(sys.argv[1])[0])
with open(result_filename, 'w') as f:
    f.write(text)
