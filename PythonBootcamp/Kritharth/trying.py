def div(m , n):
    res = 0
    try:
         res = m/n
    
    except(ValueError,TypeError,ZeroDivisionError):
        print("Something went wrong!\nEnter two numbers:")
        m = int(input("m = "))
        n = int(input("n = "))
        div(m,n)


    else:
        print("The result of the division is: ",res)

    finally:
        print("Mission Complete\nRespect++\n")

    

m = int(input("Enter a value:"))
n = int(input("Enter b value:"))
div(m,n)
