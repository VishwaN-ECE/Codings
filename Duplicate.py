text="Hello world"
res=" "
for char in text:
    if char not in res:
        res=res+char
print(res)
