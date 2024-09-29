a=[6,8,10]
n=int(input())
b=2
for x in range(2,n):
    b+=8
    if x%2==0:
        a.append(a[x]+b)
    else :
        a.append(a[x]+b)
for x in range(n):
    if x%2==0:
        print(f'{a[x]}')
    else:
        print(f'-{a[x]}')