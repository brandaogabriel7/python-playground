import random

def mergeSort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left_array = array[:middle]
        right_array = array[middle:]

        mergeSort(left_array)
        mergeSort(right_array)

        left_index = right_index = main_index = 0

        while left_index < len(left_array) and right_index < len(right_array):
            if left_array[left_index] < right_array[right_index]:
                array[main_index] = left_array[left_index]
                left_index += 1
            else:
                array[main_index] = right_array[right_index]
                right_index += 1
            main_index += 1

        while left_index < len(left_array):
            array[main_index] = left_array[left_index]
            left_index += 1
            main_index += 1

        while right_index < len(right_array):
            array[main_index] = right_array[right_index]
            right_index += 1
            main_index += 1


items = []

for i in range(10):
    items.append(random.randint(0, 1000))

print(items)

mergeSort(items)

print(items)
