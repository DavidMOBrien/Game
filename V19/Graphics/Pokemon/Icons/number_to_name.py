import os
import shutil

with open('mapped_pokemon.txt', 'r') as inputFile:
    dataset = inputFile.readlines()

table = {}

for item in dataset:
    number = 'icon' + item[0:3] + '.png'
    internalname = item[4:].strip('\n') + '.png'

    table[number] = internalname

files = []

for item in os.listdir():
    files.append(item)


for item in files:
    item = str(item)

    if item in table:
        shutil.move(item, table[item])
