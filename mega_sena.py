from random import randint

b = set()

while len(b) < 6:
    b.add(randint(1, 60))

b = list(b)
print(b)
