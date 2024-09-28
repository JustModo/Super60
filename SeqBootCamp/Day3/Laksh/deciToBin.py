decimal = int(input("Enter Decimal Number: "))
binary=0
rem=0
base=1

while(decimal>0):
    rem = decimal%2
    binary = int(binary+rem*base)
    decimal=int(decimal/2)
    base*=10

print(binary)