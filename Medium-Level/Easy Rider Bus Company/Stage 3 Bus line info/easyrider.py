import json
import re


easy_bd = json.loads(input())

lines = {}

for data in easy_bd:
    lines[data["bus_id"]] = (lines[data["bus_id"]] + 1) if lines.get(data["bus_id"], False) else 1

print(f'Line names and number of stops:')
for field in lines:
    print(f'bus_id: {field}, stops: {lines[field]}')
