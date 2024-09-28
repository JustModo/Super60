a=[6,8,10]
n=int(input())
c=1
for x in range(2,n+1):
    b=(a[x]-a[x-1] )+(a[x-1]-a[x-2])
    a.append(a[x]+b)
  
for x in range(n):
    if x%2==0:
        print(f'{a[x]}')
    else:
        print(f'-{a[x]}')