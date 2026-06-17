text="{{}[]()}"
l=list(text)
n=len(l)
stack=[]
count=0
for i in l:
    if i=="{" or i=="[" or i=="(":
        stack.append(i)
    elif i=="}":
        if len(stack)==0 or stack.pop()!="{":
            count=count+1
    elif i=="]":
        if  len(stack)==0 or stack.pop()!="[":
            count=count+1
    elif i==")":
        if len(stack)==0 or stack.pop()!="(":
            count=count+1
if count!=0 or len(stack)!=0:
    print("unbalanced")
else:
    print("balanced")
