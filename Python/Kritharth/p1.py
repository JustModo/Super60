# 4,16,36,64,.....,n
n = int(input("Enter n value: "))
start = 2
for _ in range(n):
    print(start*start)
    start+=2