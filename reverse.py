text="python"
l=list(text)
n=len(l)
for i in range(n//2):
    temp=l[i]
    l[i]=l[n-1-i]
    l[n-1-i]=temp
    reverse="".join(l)
print(reverse)
    
