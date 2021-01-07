# CHANGE INTEGER TO STRING ALGORITHM

inputInt = 123 # return "123"

def intToStr(i):
    if i < 0:
        isNegative = True
        i *= -1
    else:
        isNegative = False

    # assign empty list to store the output
    outputStr = []
    while i > 0:
        # store the num to outputStr
        outputStr.append(chr(ord('0') + i % 10))
        i //= 10
    
    # reverse the elements of the list
    outputStr = outputStr[::-1]
    # remove the (,)
    outputStr = "".join(outputStr)

    # check if the int is negative
    # then add (-) to the output
    if isNegative:
        return "-" + outputStr
    else:
        return outputStr

print(intToStr(inputInt))
print(intToStr(-123))

