import random

def color(x, y, data):
    g = open(data, "r")
    ra = random.randint(x, y)
    for lines in g:
        a = int(lines[0])
        if a == ra:
            return lines[2:]

print(color(1,5,"color.txt"))