# 6 -8 10 -14 20 -30 46
#  2  2  4   6  10

numbers = [6,8,10]

for i in range(1,16):
    sumDiff = (numbers[1]-numbers[0])+(numbers[2]-numbers[1])
    if i%2==0:
        print(f"-{numbers[0]}", end=" ")
    else:
        print(numbers[0], end=" ")
    numbers.pop(0)
    numbers.append(numbers[1]+sumDiff)