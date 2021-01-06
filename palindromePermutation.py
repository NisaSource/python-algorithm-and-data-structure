# Palindrome Permutation algorithm

# Palindrome -> A word spelled the same way forward and backward
# Permutation -> An ordering of set of item

str1 = "rceraca"
str2 = "we love python"

def isPalindromePermutation(s):
    # Ignore the space and turn it to lowercase
    s = s.replace(" ", "")
    s = s.lower()

    # Create new hash which will hold number of chars
    h = dict()

    # Iterate through the strings and save it to the hash
    for i in s:
        if i in h:
            h[i] += 1
        else:
            h[i] = 1

    # Check the nums of chars that appear an odd nums of times
    oddCount = 0
    for k, v in h.items():
        if v % 2 != 0 and oddCount == 0:
            oddCount += 1
        elif v % 2 != 0 and oddCount != 0:
            return False
    return True

print(isPalindromePermutation(str1))
print(isPalindromePermutation(str2))
