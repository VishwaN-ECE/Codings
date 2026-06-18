n=int(input("enter the number:"))
while n>=10:
    sum=0
    for char in str(n):
        sum=sum+int(char)
        n=sum
print(n)
