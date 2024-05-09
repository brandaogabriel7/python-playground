import random

items = []

for i in range(10):
    items.append(random.randint(0, 1000))

print(items)

first_unsorted = 0

while first_unsorted < len(items) - 1:
    minimum_index = first_unsorted
    for i in range(first_unsorted + 1, len(items)):
        if items[i] < items[minimum_index]:
            minimum_index = i

    aux = items[minimum_index]
    items[minimum_index] = items[first_unsorted]
    items[first_unsorted] = aux

    first_unsorted +=1

print(items)