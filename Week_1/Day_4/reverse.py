s=input("Enter a string:")
left=0
right=len(s)-1
l=list(s)
while left<right:
    l[left],l[right]=l[right],l[left]
    left=left+1
    right=right-1
s1=""
for i in l:
    s1 +=i
print("Reverse of a string:"+s1)