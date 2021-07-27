import os

files = []

for item in os.listdir():
    files.append(item)


for item in files:
    if 'icon' in item and 'fix' not in item:
        os.rename(item, item[4:])