text="Mepco"
vowels="aeiouAEIOU"
remove="".join([i for i in text if i not in vowels])
print(remove)
