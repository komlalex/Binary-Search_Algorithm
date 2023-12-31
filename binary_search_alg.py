def binary_search(list, target):
    first = 0
    last = len(list) - 1
    
    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def rec_binary_search(list, target): 
    if len (list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == target:
            return True
        elif list[midpoint] < target:
            return rec_binary_search(list[midpoint+1:], target)
        else:
            return rec_binary_search(list[:midpoint], target)



numbers = [1,2,3,4,5,6,7,8]

result = binary_search(numbers, 34)

print(result)