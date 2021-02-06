import json
import itertools

easy_db = json.loads(input())

stops = dict()
lines = dict()
prev_id = easy_db[0]["bus_id"]
error = False

for data in easy_db:
    curr_id = data["bus_id"]

    if curr_id not in lines:
        lines[curr_id] = [set(), set()]
    lines[curr_id][0].add(data["stop_type"])
    lines[curr_id][1].add(data["stop_name"])

    if data["stop_type"] not in stops:
        stops[data["stop_type"]] = set()
    stops[data["stop_type"]].add(data["stop_name"])

for line in lines:
    if not {'S', 'F'}.issubset(lines[line][0]):
        error = True
        print(f"There is no start or end stop for the line: {line}")
        break

pairs = itertools.combinations([lines[line][1] for line in lines], 2)
transfer_stops = set()
for pair in pairs:
    transfer_stops.update(set.intersection(*pair))

if not error:
    print(f"Start stops: {len(stops['S'])} {sorted(list(stops['S']))}")
    print(f"Transfer stops: {len(transfer_stops)} {sorted(list(transfer_stops))}")
    print(f"Finish stops: {len(stops['F'])} {sorted(list(stops['F']))}")
