
data = [2,5,7,8,9,13,16,18,23,27,36]
num = 16

# 1. FIND VALUE IN AN ARRAY
# Using Linear Search
def linarSearch(data, num):
    for i in range(len(data)):
        if data[i] == num:
            return i
    return -1

print(linarSearch(data, num))

# Using Binary Search
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


# 2. FIND CLOSEST NUMBER
# Using Binary Search
def findClosestNumber(arr, num):
    minDiff = float("inf")
    start = 0
    end = len(arr) - 1
    closestNum = None

    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    
    while start <= end:
        mid = (start + end) // 2

        if mid + 1 < len(arr):
            right = abs(arr[mid+1] - num)
        if mid > 0:
            left = abs(arr[mid-1] - num)
        
        if left < minDiff:
            minDiff = left
            closestNum = arr[mid - 1]

        if right < minDiff:
            minDiff = right
            closestNum = arr[mid + 1]

        if arr[mid] < num:
            start = mid + 1
        elif arr[mid] > num:
            end = mid - 1
        else:
            return arr[mid]
    
    return closestNum


print(findClosestNumber(data, 40))

# 3. FIND FIXED POINT
# Fixed point -> same value of A[i] and i

A = [-3,0,2,5,8,9] # return 2
A1 =  [-1,2,3,5,7,9] # return None

# Using Linear Search
def findFixedPoint(a):
    for i in range(len(a)):
        if a[i] == i:
            return a[i]
    return None
print(findFixedPoint(A))
print(findFixedPoint(A1))

# Using Binary Search
def findFixedPointBinarySearch(a):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2

        if a[mid] < mid:
            start = mid + 1
        elif a[mid] > mid:
            end = mid - 1
        else:
            return a[mid]
    return None

print(findFixedPointBinarySearch(A))
print(findFixedPointBinarySearch(A1))


# 4. FIND HIGHEST NUMBER FROM BITONIC SEQUENCE
# Bitonic sequence -> [1,2,3,4,5,4,3,2,1]

A = [1,2,3,4,3,2,1] # return 4
B = [1,2,3,1] # rerurn 3
C = [1,7,6,5,4,3,2,1] # return 7

#Using Binary search
def findHighestNumber(a):
    # Check lenght of the seq should be at least 3
    if len(a) < 3: return None

    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        left = a[mid - 1] if mid - 1 > 0 else float("-inf")
        right = a[mid + 1] if mid + 1 < len(a) else float("inf")

        if left < a[mid] and right > a[mid]:
            start = mid + 1
        elif left > a[mid] and right < a[mid]:
            end = mid - 1
        elif left < a[mid] and right < a[mid]:
            return a[mid]

print(findHighestNumber(A))
print(findHighestNumber(B))
print(findHighestNumber(C))


# 5. SQUARE ROOT ALGORITHM

N = 90 # return 9, bcs 9*9 = 81 which is the closest to 90

# Using Binary Search
def squareRootInt(n):
    start = 0
    end = n

    while start <= end:
        mid = (start + end) // 2
        midSquared = mid * mid

        if midSquared <= n:
            start = mid + 1
        else:
            end = mid - 1
    return start - 1

print(squareRootInt(N))
