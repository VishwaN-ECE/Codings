n=int(input("enter the number:"))
l=len(str(n))
original=n
total=0
while n>0:
    digit=n%10
    total=total+(digit**l)
    n=(n//10)
if total==original:
    print("amstrong")
else:
    print("no")
