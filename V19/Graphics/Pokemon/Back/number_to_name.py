import os
import shutil

with open('mapped_pokemon.txt', 'r') as inputFile:
    dataset = inputFile.readlines()

table = {}

for item in dataset:
    number = item[0:3] + '.png'
    shadow_number = item[0:3] + '_shadow.png'
    internalname = item[4:].strip('\n') + '.png'
    shadow_int = item[4:].strip('\n') + '_shadow.png'

    table[number] = internalname
    table[shadow_number] = shadow_int

files = []

for item in os.listdir():
    files.append(item)


for item in files:
    item = str(item)

    if item in table:
        shutil.move(item, table[item])
