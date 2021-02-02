import json
import re


easy_bd = json.loads(input())
errors = {"stop_name": [0, (r"[A-Z].* Road\Z", r"[A-Z].* Avenue\Z", r"[A-Z].* Boulevard\Z", r"[A-Z].* Street\Z")],
          "stop_type": [0, (r"F?\Z", r"O?\Z", r"S?\Z")],
          "a_time": [0, (r"[0-1][0-9]:[0-5][0-9]\Z", r"2[0-4]:[0-5][0-9]\Z")]}
for data in easy_bd:
    for field in errors:
        match = False
        for template in errors[field][1]:
            if re.match(template, data[field]):
                match = True
        if not match:
            errors[field][0] += 1


print(f'Type and required field validation: {sum(value[0] for value in errors.values())} errors')
for field in errors:
    print(f'{field}: {errors[field][0]}')
