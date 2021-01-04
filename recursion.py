# 1. Find First Upper Case Character

str1 = "iLovepython" # return L
str2 = "ilovePython" # return P
str3 = "ilovepython" # return "No uppercase string"

def firstUpperCase(inputStr, idx = 0):
    if inputStr[idx].isupper():
        return inputStr[idx]
    if idx == len(inputStr) - 1:
        return "No uppercase string"
    return firstUpperCase(inputStr, idx + 1)

print(firstUpperCase(str1))
print(firstUpperCase(str2))
print(firstUpperCase(str3))
