# Download the data
import json 
import os
import requests
import urllib.request

# Opening JSON file 
dire = 'n6'
f_red = open('n6.json')
data = json.load(f_red)
if not os.path.exists(dire):
    os.mkdir(dire)
filename_index = 500
for key in data['images_results']:
    url = data['images_results'][key]['original']
    extension = url[-4:]
    if extension == '.jpg' or extension == '.png':
        filename = f'{dire}/{str(filename_index)}{extension}'
    else:
        filename = f'{dire}/{str(filename_index)}.jpg'
    try:
        urllib.request.urlretrieve(url, filename)
        print(filename)
        filename_index += 1
    except:
        continue