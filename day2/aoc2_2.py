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

# A, X = 'rock' loss
# B, Y = 'paper' draw 
# C, Z = 'scissor' win

with open('day2\input.txt') as f:
    data = f.read()
    match2 = 0
    for line in data.splitlines():
        at, strategy = line.split(' ')
        if strategy == 'X':
            df = losses[at]
            match2 += score[df]
        elif strategy == 'Y':
            df = draw[at]
            match2 += score[df] + 3
        else:
            df = wins[at]
            match2 += score[df] + 6
    print(match2)