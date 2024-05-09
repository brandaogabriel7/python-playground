import random

items = []

for i in range(10):
    items.append(random.randint(0, 1000))

print(items)

lastSortedIndex = len(items)

while True:
    swapped = False
    for i in range(1, lastSortedIndex):
        if items[i-1] > items[i]:
            aux = items[i]
            items[i] = items[i-1]
            items[i-1] = aux

            swapped = True
        if i == lastSortedIndex - 1:
            lastSortedIndex = i
    if not swapped:
        break

print(items)