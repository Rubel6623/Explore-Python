listr = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
listr[2][1][2].extend(sub_list)
print(listr)
print(end='\n')
#replace item

a=[5,10,15,20,25,50,20]
a[3]=200
print(a)
print(end='\n')

#remove item

list1 = [5, 20, 15, 20, 25, 50, 20]
x=list()
for i in list1:
    if i==20:
        continue
    x.append(i)
print(x)

"""
<-----or----->
list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)
print(list1)
"""