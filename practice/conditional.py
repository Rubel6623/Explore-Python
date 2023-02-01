#AND
num1=45
num2=78
num3=21
if num1>num2 and num1>num3:
    print("max =",num1)
elif num2>num1 and num2>num3:
    print("max =",num2)
else:
    print("max =",num3)

    #OR
ch=input("enter any letter :")
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("vowel")
else:
     print("consonent")

#conditional demo

mark=int(input("Enter Your Mark :"))
if mark>=80 and mark<=100:
    print("A+")
elif mark>=70 and mark<=79:
    print("A")
elif mark>=60 and mark<=69:
    print("A-")
elif mark>=50 and mark<=59:
    print("B")
elif mark>=40 and mark<=49:
    print("C")
elif mark>=33 and mark<=39:
    print("D")
else:
    print("Fail")