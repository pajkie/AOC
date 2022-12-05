from aocd import get_data
d = get_data(day=4, year=2022).split("\n")

p = 0
for x in d:
    one, two = x.split(",")
    one = one.split("-")
    two = two.split("-")

    if int(one[0]) in range(int(two[0]), int(two[1])+1) or int(one[1]) in range(int(two[0]), int(two[1])+1):
        p += 1
    elif int(two[0]) in range(int(one[0]), int(one[1])+1) or int(two[1] in range(int(one[0]), int(one[1])+1)):
        p += 1

print(p)
