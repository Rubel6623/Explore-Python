num=int(input("Enter a number :"))
reverse=0
while num>0:
    reminder=num%10
    reverse=(reverse*10)+reminder
    num=num//10
print("the reverse number is :",reverse)

#slicing
mylist=[10,20,30,40,50,60,70,80,90,100]
for i in mylist[1::2]:
    print(i,end=' ')
