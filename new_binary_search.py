def binary_search(list, target): 
    middle = 0
    start = 0
    end = len(list) - 1
    steps = 0

    while (start <= end):
        print(f"Steps: {steps}, list: {str(list[start:end+1])}")

        steps += 1
        middle = (start + end) // 2

        if list[middle] == target:
            return middle
        elif list[middle] > target:
             end = middle - 1
        else:
            start = middle + 1

    return -1

numbers = [1,2,3,4,5,6,8,9]
target = 15
result = binary_search(numbers, target)
print(result)


