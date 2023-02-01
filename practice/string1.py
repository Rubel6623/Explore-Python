str1="james"
print("Original String is ",str1)
res=str1[0]
len=len(str1)
mid=int(len/2)
res=res+str1[mid]+str1[len-1]
print(res)