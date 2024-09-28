abc={
    0:"Zero",
    1:"One",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"Five",
    6:"Six",
    7:"Seven",
    8:"Eight",
    9:"Nine"

}
a=9210300
temp=0
z=[]
while(a>0):
    temp=a%10
    temp=int(temp)
    z.append(abc[temp])
    a/=10
    a=int(a)
z.reverse()
print(z)


