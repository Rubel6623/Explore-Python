li=[3,6,9,12,15,18,21]
li1=[4,8,12,16,20,24,28]
res=list()
odd=li[1::2]
even=li1[0::2]
print("element at odd-index positions number from list one :",odd)
print("element at even-index positions number from list one :",even)
res.extend(odd)
res.extend(even)
print("Printing the final third list :",res)
print(end='\n')

#list function

list=[54,44,27,79,91,41]
print("main List is : ",list)
remove=list.pop(4)
print("List After removing element at index 4 :",list)
adding=list.insert(2,555)
print("List after addind element at index 2 :",list)
list.append(999)
print("list after adding element at last :",list)

