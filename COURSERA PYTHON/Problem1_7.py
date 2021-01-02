def problem1_7():
    b1=int(input("Enter the length of one of the bases: "))
    b2=int(input("Enter the length of the other base: "))
    h=int(input("Enter the height: "))
    
    b1=float(b1)
    b2=float(b2)
    h=float(h)
    
    area=1/2*(b1+b2)*h
    
    print("The area of a trapezoid with bases",b1,"and",b2,"and height",h,"is",area)