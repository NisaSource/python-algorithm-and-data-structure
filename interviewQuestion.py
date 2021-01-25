# 1. Find missing number from list of number from 1 to 100


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42,
43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62,
63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82,
83, 84, 85, 86, 87, 88, 89, 90, 91, 93, 94, 95, 96, 97, 98, 99, 100]

def findMissingNum(list, n):
    sum1 = 100 * 101 / 2
    sum2 = sum(list)

    return sum1 - sum2

print(findMissingNum(myList, 100))


# 2. Given an array of integers and an integer, return indices of the two numbers
# such as they add up to the integer. Don't use the same element twice.

myList2 = [1,2,3,3,4,4,5,6]

def findPairs(list, n):
    pairs = []
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if list[i] == list[j]:
                continue
            elif list[i] + list[j] == n:
                temp = []
                temp.append(i)
                temp.append(j)
                pairs.append(temp)
    return pairs

res = findPairs(myList2, 6)
for a in res:
    print(a)


# 3. Find maximum product of two integers in the array where all elements are positive

import numpy as np

myArray = np.array([2,30,12,45,34,54,13,27,59,32,21,39,40,5,9]) #return 

def findMaxProduct(arr):
    maxProduct = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] * arr[j] > maxProduct:
                maxProduct = arr[i] * arr[j]
                pairs = str(arr[i]) + "," + str(arr[j])
    print(pairs)
    return maxProduct

print(findMaxProduct(myArray))


