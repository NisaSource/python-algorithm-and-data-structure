# 1. Write a function called middle that takes a list and 
# returns a new list that contains all but the first and last elements

myList = [1,2,3,4,5,6] #return [2,3,4,5]

def findMiddleList(list):
    return list[list[0]:list[-2]]

print(findMiddleList(myList))

# 2. Given a list, write a function to get first and second best scores from the list.

myList2 = [67,86,45,87,59,97,98,52,41] # return 98 97

def findBestScores(list):
    list.sort()
    return list[-1], list[-2]

print(findBestScores(myList2))

# 3. Write a function to find the missing number in a given integer array of 1 to 100

myList3 = [1,2,3,4,6] # return 5

def findMissingNumber(list, totalNum):
    total = totalNum * (totalNum +1)/2
    sumList = sum(list)
    return total - sumList

print(findMissingNumber(myList3, 6))

# 4. Write a function to find the duplicate number on given integer array/list

myList4 = [1,1,2,3,3,4,4,5,5] #return [1,2,3,4,5]

def removeDuplicate(list):
    newList = []
    for i in range(len(list)):
        if list[i] in newList:
            continue
        else:
            newList.append(list[i])
    return newList

print(removeDuplicate(myList4))


# 5. Write a function to find all pairs of an integer array whose sum is equal to given number

myList5 = [2,4,1,5,3,-3,9]

def pairSum(list, sum):
    newList = []
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            temp = list[i] + list[j]
            if temp == sum:
                newList.append(str(list[i]) + "+" + str(list[j]))
    return newList


print(pairSum(myList5, 6))
