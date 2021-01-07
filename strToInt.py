# CHANGE STRING TO INTEGER ALGORITHM

S = "349" # return 349

def strToInt(s):
    outputInt = 0

    if s[0] == "-":
        start = 1
        isNegative = True
    else:
        start = 0
        isNegative = False

    for i in range(start, len(s)):
        place = 10**(len(s) - (i+1))
        digit = ord(s[i]) - ord('0')
        outputInt += place * digit

    if isNegative:
        return -1 * outputInt
    else:
        return outputInt

print(strToInt(S))