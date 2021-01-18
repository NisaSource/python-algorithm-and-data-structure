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

# N = 12 return 3
# N = 123 return 6

def sumOfDigits(n):
    assert n >= 0 and int(n) == n , "ONLY POSITIVE NUMBER!"
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(int(n/10))

print(sumOfDigits(12))


# 5. Calculate the power of number

# N = 2, E = 3 return 8
# N = 3, E = 4 return 81

def powerOfNum(n, e):
    assert e >= 0 and int(e) == e, "ONLY POSITIVE NUMBER!"
    if e == 0:
        return 1
    if e == 1:
        return n
    return n * powerOfNum(n, e-1)

print(powerOfNum(3, 4))


# 6. Great Common Divisor (GCD)

# A = 20, B = 12 return 4
# A = 326, B = 278 return 2

def greatCommonDivisor(a, b):
    assert int(a) == a and int(b) == b, "ONLY POSITIVE INTEGER!"
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    if b == 0:
        return a
    else:
        return greatCommonDivisor(b, a % b)

print(greatCommonDivisor(326, 278))


# 7. Decimal to Binary

# N = 10 return 1010

def decimalToBinary(n):
    assert int(n) == n, "ONLY POSITIVE INTEGER!"
    if n == 0:
        return 0
    return (n % 2) + (10 * decimalToBinary(int(n / 2)))

print(decimalToBinary(10))

# 8. String Reverse

S = "python" # return "nohtyp"

def reverseStr(strng):
    if len(strng) <= 1:
        return strng
    print(strng[0:len(strng)-1])
    return strng[len(strng) - 1] + reverseStr(strng[0:len(strng)-1])

print(reverseStr(S))

# 8. Palindrome

string1 = "awesome" # return false
string2 = "tacocat" # return true 

def isPalindrome(s):
    if len(s) == 0:
        return True
    if s[0] != s[len(s)-1]:
        return False
    return isPalindrome(s[1:-1])

print(isPalindrome(string1))
print(isPalindrome(string2))


""" 9. Write a recursive function called someRecursive which accepts an array and a callback.
The function returns true if a single value in the array returns true when passed to the
callback. Otherwise it returns false. """

arr1 = [1,2,3,4] # return true
arr2 = [2,4,6,8] # return false

def isOdd(n):
    if n % 2 == 0:
        return False
    return True

def someRecursive(arr, cb):
    if len(arr) == 0:
        return False
    if not (cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True

print(someRecursive(arr1, isOdd))
print(someRecursive(arr2, isOdd))


# 10. Write a recursive function called flatten which accepts an array of arrays and return
# a new array with all values flattened.

a1 = [1,2,3,[4,5,6,7]] # return [1,2,3,4,5,6,7]
a2 = [1,2,[3,[4,5],6,7]] # return [1,2,3,4,5,6,7]

def flatten(a):
    result = []
    for item in a:
        if type(item) is list:
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten(a1))
print(flatten(a2))


# 11. Write a recursive function called capitalizeFirst. Given an array
# of strings, capitalize the first letter of each string in the array.

A = ["cat", "dog", "monkey"] # return ["Cat", "Dog", "Monkey"]

def capitalizeFirst(a):
    result = []
    if len(a) == 0:
        return result
    str = a[0]
    result.append(str[0].upper() + str[1:])
    return result + capitalizeFirst(a[1:])

print(capitalizeFirst(A))


# 12. Write a recursive function called nestedEvenSum. Return the sum of all
# even numbers in an object which may contain nested objects

obj1 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
} # return 10

def nestedEvenSum(obj, sum=0):
    for k in obj:
        if type(obj[k]) is dict:
            sum += nestedEvenSum(obj[k])
        if type(obj[k]) is int and obj[k] % 2 == 0:
            sum += obj[k]
    return sum

print(nestedEvenSum(obj1))

# 13. Write a function called stringifyNumbers which takes an object and finds all
# of the values which are numbers and converts them to strings.

obj2 = { "num": 1, "test": [], "data": {"val": 4, "info": {"isRight": True, "random": 66}}}
# return { "num": "1", "test": [], "data": {"val": "4", "info": {"isRight": True, "random": "66"}}}

def stringifyNumbers(obj):
    newObj = obj
    for k in newObj:
        if type(newObj[k]) is int:
            newObj[k] = str(newObj[k])
        elif type(newObj[k]) is dict:
            newObj[k] = stringifyNumbers(newObj[k])
    return newObj

print(stringifyNumbers(obj2))