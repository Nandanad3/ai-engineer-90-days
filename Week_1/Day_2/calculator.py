a=int(input("Enter a number1:"))
b=int(input("Enter a number2:"))
o=input("Enter operator:")

if o=="+":
    print(a+b)
elif o=="-":
    print(a-b)
elif o=="*":
    print(a*b)
elif o=="/":
    print(a/b)
elif o=="%":
    print(a%b)
elif o=="**":
    print(a**b)
else:
    print("Invalid choice")