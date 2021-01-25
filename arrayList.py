# 1. Write a function called middle that takes a list and 
# returns a new list that contains all but the first and last elements

myList = [1,2,3,4,5,6] #return [2,3,4,5]

def middle(list):
    return list[list[0]:list[-2]]

print(middle(myList))
