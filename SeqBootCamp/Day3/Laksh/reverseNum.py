def numToWords(number)->None:
    match number:
        case 1: print("one", end=" ")
        case 2: print("two", end=" ")
        case 3: print("three", end=" ")
        case 4: print("four", end=" ")
        case 5: print("five", end=" ")
        case 6: print("six", end=" ")
        case 7: print("seven", end=" ")
        case 8: print("eight", end=" ")
        case 9: print("nine", end=" ")
        case 0: print("zero", end=" ")


num = input("Enter Number: ")
num = list(reversed(num))
#remove trailing
while(num[0]=='0'):
    num.pop(0)

for digit in num:
    try:
        numToWords(int(digit))
    except ValueError:
        print("NaN", end=" ")