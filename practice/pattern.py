"""
*
**
***
****
"""
n=4
for i in range(1,n+1,1):
    for j in range(1,i+1):
        print(j,end=' ')
    print("")

"""
*
***
*****
*******
(2*i-1)
"""
n=5
for i in range(n+1):
    print((2*i-1)*"*")

"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""
a=5
k=5
for i in range(0,a+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()