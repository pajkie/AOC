#d1_p1
with open('day1\input.txt') as f:
    data = f.read()

    cal = 0

    for x in data.split("\n\n"):
        total = 0
        
        for y in x.splitlines():
            total += int(y)
        
        cal = max(cal, total)
    print(cal)

        
