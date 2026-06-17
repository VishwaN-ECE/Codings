text="10010101010010100"
l=list(text)
stack=[]
stack1=[]
for i in l:
    if i=="0":
        stack.append(i)
    elif i=="1":
        stack1.append(i)
res=stack+stack1
print(str(res))
