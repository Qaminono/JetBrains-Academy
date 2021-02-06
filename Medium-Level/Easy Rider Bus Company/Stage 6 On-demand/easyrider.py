import json

easy_db = json.loads(input())

stops = dict()

for data in easy_db:
    if data["stop_name"] not in stops:
        stops[data["stop_name"]] = set()
    stops[data["stop_name"]].add(data["stop_type"])

errors = list()

for stop in stops:
    if len(stops[stop]) >= 2 and "O" in stops[stop]:
        errors.append(stop)

print("On demand stops test:")
if errors:
    print(f"Wrong stop type: {sorted(errors)}")
else:
    print("OK")
