import random

items = [random.randint(0, 100) for i in range(10)]

print(items)

# insertion
# for i in range(1, len(items)):
#     current = items[i]
#     for j in range(i-1, -1, -1):
#         if current < items[j]:
#             items[j+1] = items[j]
#             if j == 0:
#                 items[j] = current
#         else:
#             items[j+1] = current
#             break

# selection

# first_unsorted = 0

# while (first_unsorted < len(items) - 1):
#     minimum_index = first_unsorted
#     for i in range(first_unsorted + 1, len(items)):
#         if items[i] < items[minimum_index]:
#             minimum_index = i

#     aux = items[minimum_index]
#     items[minimum_index] = items[first_unsorted]
#     items[first_unsorted] = aux

#     first_unsorted += 1

# merge sort
# def mergeSort(array):
#     if len(array) > 1:
#         middle = len(array) // 2
#         left_array = array[:middle]
#         right_array = array[middle:]

#         mergeSort(left_array)
#         mergeSort(right_array)

#         main_index = left_index = right_index = 0

#         while left_index < len(left_array) and right_index < len(right_array):
#             if left_array[left_index] < right_array[right_index]:
#                 array[main_index] = left_array[left_index]
#                 left_index += 1
#             else:
#                 array[main_index] = right_array[right_index]
#                 right_index += 1
#             main_index += 1

#         while left_index < len(left_array):
#             array[main_index] = left_array[left_index]
#             left_index += 1
#             main_index += 1

#         while right_index < len(right_array):
#             array[main_index] = right_array[right_index]
#             right_index += 1
#             main_index += 1
        
# mergeSort(items)
    
# bubble sort

lastSortedIndex = len(items)

while True:
    swapped = False

    for i in range(1, lastSortedIndex):
        if items[i] < items[i-1]:
            aux = items[i]
            items[i] = items[i-1]
            items[i-1] = aux

            swapped = True

        if i == lastSortedIndex - 1:
            lastSortedIndex = i
    
    if not swapped:
        break

print(items)