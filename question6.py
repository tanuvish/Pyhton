a=int(input("enter first number :"))
b=int(input("enter second number :"))
c=int(input("enter third number :"))
max = "first number"if (a>b and a>c) else "second number" if b>c else "third number"
print("greatest number is :",max)
