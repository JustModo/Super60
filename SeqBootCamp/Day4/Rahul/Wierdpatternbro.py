a=[1,5]
n=int(input())
b=4
for x in range(1,n):
    b+=5
    a.append(a[x]+b)
print(a)


