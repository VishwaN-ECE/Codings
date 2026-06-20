n=int(input("enter the number:"))
factors=0
for i in range(1,n+1):
    if n%i==0:
        factors=factors+1
if factors==2:
    print("prime number")
else:
    print("no")
