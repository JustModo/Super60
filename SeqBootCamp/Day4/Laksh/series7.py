nums = [1,1]
sign = 1

for i in range(1,6):
    for j in range(0, i):
        if sign%2==0:
            print(f"-{nums[0]}", end=" ")
        else:
            print(nums[0], end=" ")
        nextNum = sum(nums)
        sign+=1
        nums.pop(0)
        nums.append(nextNum)
    print("\n")
