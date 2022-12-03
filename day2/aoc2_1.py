score = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}


wins = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X',
}

losses  = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y',
}

draw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
}

with open('day2\input.txt') as f:
    data = f.read()
    match = 0
    for line in data.splitlines():
        at, df = line.split(' ')

        match += score[df]
        if wins[at] == df:
            match += 6
        elif losses[at] == df:
            match += 0
        else:
            match += 3
    print(match)