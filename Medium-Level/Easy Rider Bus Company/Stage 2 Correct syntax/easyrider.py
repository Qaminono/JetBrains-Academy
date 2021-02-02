import json
import re


easy_bd = json.loads(input())
errors = {"stop_name": [0, r"\A[A-Z].*[a-z] (Road|Avenue|Boulevard|Street)\Z"],
          "stop_type": [0, r"\A[FOS]?\Z"],
          "a_time": [0, r"\A([0-1][0-9]|2[0-3]):[0-5][0-9]\Z"]}
for data in easy_bd:
    for field in errors:
        if not re.match(errors[field][1], data[field]):
            errors[field][0] += 1

print(f'Type and required field validation: {sum(value[0] for value in errors.values())} errors')
for field in errors:
    print(f'{field}: {errors[field][0]}')
