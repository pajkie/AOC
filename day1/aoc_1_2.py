# d1_p2
with open('input.txt') as f:
    data = f.read()
    cal = []

    for x in data.split("\n\n"):
        total = 0

        for y in x.splitlines():
            total += int(y)

        cal.append(total)

    print(sum(sorted(cal, reverse=True)[:3]))
