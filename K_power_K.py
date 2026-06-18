n=int(input("enter the number:"))
target=[2**2, 3**3, 4**4]
found=False
for i in range(4):
    k=n-(i*i)
    if k in target:
        found=True
    else:
        found=False
print(found)
