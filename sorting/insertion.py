import random

items = []

for i in range(10):
    items.append(random.randint(0, 1000))

print(items)


for i in range(1, len(items)):
    current = items[i]
    for j in range(i-1, -1, -1):
        if items[j] >= current:
            items[j+1] = items[j]
            if j == 0:
                items[j] = current
        else:
            items[j+1] = current
            break

print(items)