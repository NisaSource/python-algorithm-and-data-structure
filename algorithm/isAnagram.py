# Is Anagram algorithm

str1 = "Eleven plus two"
str2 = "Twelve plus one"

def isAnagram(s1, s2):
    hashTbl = dict()

    if len(s1) != len(s2): return False
    for i in s1.lower():
        if i in hashTbl:
            hashTbl[i] += 1
        else:
            hashTbl[i] = 1

    for i in s2.lower():
        if i in hashTbl:
            hashTbl[i] -= 1
        else:
            hashTbl[i] = 1
    
    for i in hashTbl:
        if hashTbl[i] != 0: return False
    
    return True

print(isAnagram(str1, str2))
