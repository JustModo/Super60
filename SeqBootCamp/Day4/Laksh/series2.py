#1 3 5 9 15 25 41 67 109 177
# 2 2 4 6  10

nums = [1,3,5]
print(nums[0], nums[1], end=" ")
for _ in range(10):
    sumDiff = (nums[1]-nums[0])+(nums[2]-nums[1])
    nextNum = nums[2]+sumDiff
    nums.pop(0)
    nums.append(nextNum)
    print(nums[-1], end=" ")
