#make a new string from given string(with first,middle and last charac)
text="rudra"
print("Original string is :", text)
res=text[0]
l=len(text)
mid=int(l/2)
res=res+text[mid]
res=res+text[l-1]
print("New String is :",res)

#another(find mid string)

str1="JhonDipPeta"
print("Original string is :",str1)
lenth=len(str1)
mid1=int(lenth/2)
res1=str1[mid1]
res1=str1[mid1-1]+res1
res1=res1+str1[mid1+1]
print("New string is :",res1)

#Another (mid stirng)

str2="JaSonAy"
print("Original String is :",str2)
len1=len(str2)
mid2=int(len1/2)
print(str2[mid2])
res2=str2[mid2-1]+str2[mid2]+str2[mid+2]
print("New string is ;",res2)