import os

with open('trainertypes.txt', 'r') as inputFile:
    dataset = inputFile.readlines()

map = {}

for item in dataset:
    item = item.split(',')
    
    if len(item) > 1:
        num = item[0]
        name = item[1]

        with open('trainers_mapped.txt', 'a') as outputFile:
            outputFile.write(num + ',' + name + '\n')


