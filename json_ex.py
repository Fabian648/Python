from types import *
import json


j = str(input("Gib die Datei ein: "))

with open(j) as f:
    data = json.load(f)

print(data)

for l in data:
    for i, k in data[l].items():
        print(i, k)
        if isinstance(k, int) or isinstance(k, float):
            k += 1
            data[l][i] = k

print(data)

with open(j, "w") as fout:
    fout.write(json.dumps(data, indent=4))
