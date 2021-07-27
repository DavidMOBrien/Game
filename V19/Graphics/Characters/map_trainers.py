import os

with open('trainers_mapped.txt', 'r') as inputFile:
    dataset = inputFile.readlines()

map = {}

for item in dataset:
    item = item.split(',')

    map[item[0]] = item[1].strip('\n')

for item in os.listdir():

    temp = item[6:].strip('0')
    temp = temp.strip('.png')

    if 'trchar' in item:
        if temp in map:
            os.rename(item,'trainer_' + map[temp] + '.png')