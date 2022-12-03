"""
example input:
A Z
C X
A Z
A Z
C Y
C Y
"""

# X = 1 #rock
# Y = 2 #paper
# Z = 3 #scissor

# A = 'rock'
# B = 'paper'
# C = 'scissor'


won = 6
draw = 3
lost = 0


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

with open('input.txt') as f:
    data = f.read()

    for line in data:
        at, df = line.split(' ')
        print(at)
