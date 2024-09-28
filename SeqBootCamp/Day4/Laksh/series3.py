#1 -4 15 -34 61 -96 139 -190
# 3  11 19  27 35  
diff = 3
number = 1

for i in range(1,11):
    if(i%2==0):
        print(f"-{number}", end=" ")
    else:
        print(number, end=" ")
    number+=diff
    diff+=8