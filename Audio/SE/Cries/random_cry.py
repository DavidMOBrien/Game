import os
import shutil
import random

import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]

files.pop(-1)

for i in range(650,846):

    index = random.randint(0,len(files)-1)

    toCopy = files.pop(index)

    dst_dir="C:\\Users\\obrie\\Desktop\\Games\\Game\\Audio\\SE\\Cries\\" + str(i) +"Cry.wav"
    src_dir="C:\\Users\\obrie\\Desktop\\Games\\Game\\Audio\\SE\\Cries\\" + toCopy
    shutil.copy(src_dir,dst_dir)

    print("Using " + toCopy + " to create " + str(i))

with open("remaining_cries.txt", 'w') as outputFile:
    for item in files:
        outputFile.write(item)
        outputFile.write('\n')