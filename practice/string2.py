s1="Ault"
s2="Kelly"
lenth=len(s1)
mid=int(lenth/2)
res=s1[:mid]+s2+s1[mid:]
print(res)

#another

st1="America"
st2="Japan"
lenth1=len(st1)
lenth2=len(st2)
mid1=int(lenth1/2)
mid2=int(lenth2/2)
newstr=st1[0]+st2[0]+st1[mid+1]+st2[mid:]
print(newstr)

#upper case & lower case

str="PyNaTive"
lower=[]
upper=[]
for char in str:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sorted_str=''.join(lower+upper)
print(sorted_str)