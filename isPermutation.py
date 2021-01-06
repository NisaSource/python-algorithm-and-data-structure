# Permutation Algorithm

str1 = "cat"
str2 = "act"

def isPermutation(s1,s2):
    # Set all strings to lower case
    s1 = s1.lower()
    s2 = s2.lower()

    # Check the length of each strings
    if len(s1) != len(s2): return False

    # Set new dict
    d = dict()

    # Iterate through string 1 and store number of the chars to dict
    # by decreasing the existed value
    for i in s1:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1
    # Iterate through string 2 and store number of the chars to dict
    # by decreasing the existed value
    for i in s2:
        if i in d:
            d[i] -= 1
        else:
            d[i] = 1

    return all(value == 0 for value in d.values())

print(isPermutation(str1,str2))
    