# Palindrome Algorithm

str1 = "Murder for a jar of red rum" # return true
str2 = "python algorithm" # return false

def isPalindrome(inputStr):
    i = 0
    j = len(inputStr) - 1
    while i < j:
        while not inputStr[i].isalnum() and i < j:
            i += 1
        while not inputStr[j].isalnum() and i < j:
            j -= 1

        if inputStr[i].lower() != inputStr[j].lower():
            return False
        i += 1
        j -= 1
    return True

#print(isPalindrome(str1))
#print(isPalindrome(str2))

# get the string from the user and check if it's palindrome
userInput = input("Input your string : ")
print(isPalindrome(userInput))