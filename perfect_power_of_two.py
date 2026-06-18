n=int(input("enter the number:"))
if n>0 and ((n&(n-1))/2)==0:
    print("power of two")
else:
    print("no")
