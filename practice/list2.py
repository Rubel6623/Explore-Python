"""
n=input("Enter a text of numbers :")

list=n.split()
sum=0

for num in list:
    sum=sum+int(num)
print(sum)
"""

#count number of letter or number or space from given string

numOfLetter=0
numOfDigits=0
numOfSpace=0

text=input("Enter your text of numbers :")

for x in text:
    x=x.lower()
    if x>='a' and x<='z':
        numOfLetter=numOfLetter+1
    elif x>='0' and x<='9':
        numOfDigits=numOfDigits+1
    elif x==' ':
        numOfSpace=numOfSpace+1

print(numOfLetter)
print(numOfDigits)
print(numOfSpace)
