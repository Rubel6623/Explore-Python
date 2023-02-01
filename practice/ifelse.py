mark=int(input("enter your mark:"))
if mark>=33:
    print("pass")

else:
    print("fail")

num1=int(input("type any number1:\n"))
num2=int(input("type any number2:\n"))
num3=int(input("type any number3:\n"))
if num2%2==0:
    print("even \n")
else:
    print("odd \n")
if num1>num2:
    if num1>num3:
        print(num1)
    else:
        print(num3)
if num2>num1:
    if num2>num3:
         print(num2)
    else:
         print(num3)
