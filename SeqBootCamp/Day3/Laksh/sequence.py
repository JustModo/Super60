# 1 4 7 12 23 42 77 .... N

threeNums = [1,4,7]

for _ in range(15):
    print(threeNums[0])
    nextNum = sum(threeNums)
    threeNums.pop(0)
    threeNums.append(nextNum)

