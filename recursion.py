# 1. Find First Upper Case Character

str1 = "iLovepython" # return L
str2 = "ilovePython" # return P
str3 = "ilove programming" # return "No uppercase string"

def firstUpperCase(inputStr, idx = 0):
    if inputStr[idx].isupper():
        return inputStr[idx]
    if idx == len(inputStr) - 1:
        return "No uppercase"
    return firstUpperCase(inputStr, idx + 1)

print(firstUpperCase(str1))
print(firstUpperCase(str2))
print(firstUpperCase(str3))

# 2. Count consonant in the string

vowels = ["a","i","u","e","o"]

def consonantSum(inputStr):
    if inputStr == '':
        return 0
    if inputStr[0].lower() not in vowels and inputStr[0].isalpha():
        return 1 + consonantSum(inputStr[1:])
    else:
        return consonantSum(inputStr[1:])

print(consonantSum(str1))
print(consonantSum(str2))
print(consonantSum(str3))


# 3. Check palindrome word

def isPalindrome(inputStr):
    return len(inputStr) < 2 or inputStr[0] == inputStr[-1] and isPalindrome(inputStr[1:-1])

print(isPalindrome("mom"))


# 4. Sum of Digits

def sumOfDigits(n):
    assert n >= 0 and int(n) == n , "ONLY POSITIVE NUMBER!"
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(int(n/10))

print(sumOfDigits(12))