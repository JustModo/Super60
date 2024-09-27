# 1 4 7 12 23 42 77 .... N

threeNums = [1,4,7]

n = int(input("N= "))

for _ in range(n):
    print(threeNums[0], end=" ")
    nextNum = sum(threeNums)
    threeNums.pop(0)
    threeNums.append(nextNum)

