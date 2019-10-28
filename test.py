# Author Hishan Indrajith Adikari
from decimal import *
import ijson
import json

top = 7.268736
left = 80.585189
bottom = 7.250260
right = 80.612311
features = []
with open("battlefields\\roads_srilanka.json", 'r', encoding="utf8") as f:
    objects = ijson.items(f, 'features.item')
    columns = list(objects)
    print(len(columns))
    for col in columns:
        insider_found = False
        new_line = []
        elevation = col['properties']['fclass']
        if elevation not in features:
            features.append(elevation)
for feature in features:
    print(feature)
