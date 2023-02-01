list5=[100,200,300,400,500]
list5.reverse()
print(list5)

#another
list1=["M","na","i","ke"]
list2=["y","me","s","lly"]
list3=[i+j for i, j in zip(list1,list2)]
print(list3)

n=int(input())
print("{:,}".format(n))

my_str=str(input())
rev_str=reversed(my_str)
if list(my_str)==list(rev_str):
    print("Yes")
else:
    print("No")