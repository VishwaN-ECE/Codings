text="MePcO"
res=" "
for char in text:
    if char.isupper():
        res=res+char.lower()
    elif char.islower():
        res=res+char.upper()
    else:
        res=res+char
print(res)
