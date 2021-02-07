# Look and Say Sequence Algorithm

# 1      
# 11     
# 21     
# 1211   
# 111221 

def nSequence(setStr):
    result = []
    i = 0
    while i < len(setStr):
        count = 1
        while i + 1 < len(setStr) and setStr[i] == setStr[i+1]:
            i += 1
            count += 1
        result.append(str(count) + setStr[i])
        i += 1
    return "".join(result)


setStr = "1"
inputNum = input("Please input number : ")
for i in range(int(inputNum) - 1):
    setStr = nSequence(setStr)
    print(setStr)