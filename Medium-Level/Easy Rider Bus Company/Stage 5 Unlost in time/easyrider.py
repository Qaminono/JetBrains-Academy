import json

easy_db = json.loads(input())

buses_info = dict()

for bus_id in set(data["bus_id"] for data in easy_db):
    buses_info[bus_id] = [(data["stop_name"], data["a_time"]) for data in filter(lambda data: bus_id == data["bus_id"], easy_db)]

errors = list()
for bus_id in buses_info:
    prev_time = buses_info[bus_id][0][1]
    for info in buses_info[bus_id]:
        if info[1] < prev_time:
            errors.append([bus_id, info[0]])
            break
        prev_time = info[1]


print("Arrival time test:")
if errors:
    for error in errors:
        print(f"bus_id line {error[0]}: wrong time on station {error[1]}")
else:
    print("OK")
