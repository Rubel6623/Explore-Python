student=(("rudra",23,2.3),"Sumon","emon","jony")
print(student[0])
print(student[3])

#set
num={1,2,3,4,5,5}
num2=set([6,7,8,4,5])
num2.add(9)
num2.remove(6)
print(num2)
print(num | num2)
print(num & num2)
print(num-num2)

###
m=input()
n=input()
b=sorted(m)
c=sorted(n)
if b==c:
    print("Yes")
else:
    print("No")
