#1+2+3.....+n

n=int(input("enter the last number :"))
sum=0
for x in range(1,n+1,1):
    sum=sum+x
print(sum)

#2+4++6.....+n
n=int(input("enter your last number :"))
sum=0
for x in range(2,n+1,2):
    sum=sum+x
print(sum)

#1+3+5+.....+n

n=int(input("enter your last number :"))
sum=0
for x in range(1,n+1,2):
    sum=sum+x
print(sum)

#1*1+2*2+3*3+.....+n*n

n=int(input("enter your last number :"))
sum=0
for x in range(1,n+1,1):
    sum=sum+x*x
print(sum)

#1x2x3x....xn

n=int(input("enter your last number :"))
sum=1
for x in range(1,n+1,1):
    sum=sum*x
print(sum)