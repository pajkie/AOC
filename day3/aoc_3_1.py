with open('day3\input.txt') as f:
    data = f.read()
    total = 0
    for line in data.split("\n"):
        x = len(line) // 2
        a = line[:x]
        b = line[x:]
        y = set(a) & set(b)

        for k in y:
            if k.isupper():
                prio = ord(k) - 65+27
                total += prio
            else:
                prio = ord(k) - 96
                total += prio
    print(total)



