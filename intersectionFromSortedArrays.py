# Intersection from two sorted arrays

arr1 = [1,4,6,7,7,10,13]
arr2 = [4,5,5,7,11]

def intersectionSortedArray(a1,a2):
    i = 0
    j = 0
    result = []
    while i < len(a1) and j < len(a2):
        if a1[i] == a2[j]:
            if i == 0 or a1[i] != a1[i-1]:
                result.append(a1[i])
            i += 1
            j += 1
        elif a1[i] < a2[j]:
            i += 1
        else:
            j += 1
    return result

print(intersectionSortedArray(arr1,arr2))