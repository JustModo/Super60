# 1 5 13 29 49 77
number=1
multiple = 4
x=0

while(x<10):
    if (multiple%12)==0:
        multiple+=4
    else:
        print(number)
        number+=multiple
        multiple+=4
        x+=1