import json

easy_bd = json.loads(input())
errors = {"bus_id": [0, int],
          "stop_id": [0, int],
          "stop_name": [0, str],
          "next_stop": [0, int],
          "stop_type": [0, str],
          "a_time": [0, str]}
for data in easy_bd:
    for field in errors:
        if type(data[field]) != errors[field][1]:
            errors[field][0] += 1
        elif field == "stop_type" and len(data[field]) > 1:
            errors[field][0] += 1
        elif field != "stop_type" and data[field] == "":
            errors[field][0] += 1

print(f'Type and required field validation: {sum(value[0] for value in errors.values())} errors\n'
      f'bus_id: {errors["bus_id"][0]}\n'
      f'stop_id: {errors["stop_id"][0]}\n'
      f'stop_name: {errors["stop_name"][0]}\n'
      f'next_stop: {errors["next_stop"][0]}\n'
      f'stop_type: {errors["stop_type"][0]}\n'
      f'a_time: {errors["a_time"][0]}\n')
