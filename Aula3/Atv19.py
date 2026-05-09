import random

face1 = 0
face2 = 0
face3 = 0
face4 = 0
face5 = 0
face6 = 0

for i in range(100):
    dado = random.randint(1, 6)

    if dado == 1:
        face1 += 1
    elif dado == 2:
        face2 += 1
    elif dado == 3:
        face3 += 1
    elif dado == 4:
        face4 += 1
    elif dado == 5:
        face5 += 1
    else:
        face6 += 1

print("Resultado dos 100 lançamentos:")
print("Face 1:", face1)
print("Face 2:", face2)
print("Face 3:", face3)
print("Face 4:", face4)
print("Face 5:", face5)
print("Face 6:", face6)