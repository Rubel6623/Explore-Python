num=[12,75,150,180,145,525,50]
for x in num:
    if x>=525:
        break
    elif x>150:
        continue
    elif x%5==0:
        print(x)
print(end='\n')
print("end programme")

#i*n

n=2
for i in range(1,11,1):
    product=n*i
    print(product)
print(end='\n')
print("end programme")
#count digit or number

num1=75869
count=0
while num1!=0:
    num1=num1//10
    count=count+1
print("Total digits are :",count)