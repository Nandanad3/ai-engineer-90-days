n=int(input("Enter number:"))
s=n
rev=0
while n>0:
    r=n%10
    rev =rev*10+r
    n=n//10
print(rev)
if s==rev:
    print("Number is palindrome")
else:
    print("not palindrome")