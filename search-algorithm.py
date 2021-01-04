data = [2,5,7,8,9,13,16,18,23,27,36]
num = 16

# Linear Search
def linarSearch(data, num):
    for i in range(len(data)):
        if data[i] == num:
            return i
    return -1

print(linarSearch(data, num))

# Binary Search
def binarySearch(data, num):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        if num == data[mid]:
            return mid
        elif num < data[mid]:
            end = mid - 1
        else:
            start = mid + 1    
    return -1

print(binarySearch(data, num))