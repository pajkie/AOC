from aocd import get_data
data = get_data(day=3, year=2022).split("\n")

c = 3
prio = 0
total = 0
for i in range(0, len(data), 3):
    r = data[i:c]
    c += 3
    
    x = r[0]
    y = r[1]
    z = r[2]
    whatever = set(x) & set(y) & set(z)

    for e in whatever:
        if e.isupper():
            prio = ord(e) - 65+27
            total += prio
        else:
            prio = ord(e) - 96
            total += prio
print(total)