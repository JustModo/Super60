number = 1 
add = 1

for i in range(0,15):
    for _ in range(0,i):
        print(number, end=" ")
        number+=add
        add+=1  
    print("\n")