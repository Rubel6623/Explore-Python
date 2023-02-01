num1=0
num2=1
res=0
for i in range(1,11):
    print(num1,end=' ')
    res=num1+num2
    num1=num2
    num2=res
print(end='\n')

#factorial number
fac=1
num=int(input("Enter any number :"))
if num<0:
    print("Factorial does not exist for nagative number")
elif num==0:
    print("The Factorial of 0 is 1")
else:
     for j in range(1,num+1):
         fac=fac*j
     print("the factorial of",num,"is",fac)


