n=int(input("enter the number:"))
reversed=0
original=n
while n>0:
    digit=n%10
    reversed=(reversed*10)+digit
    n=n//10
if reversed==original:
    print("palindrome")
else:
    print("no")
    
