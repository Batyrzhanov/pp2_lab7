import reg

f = open('row.txt', 'r', encoding='utf-8')
text = f.read()
x = reg.findall("ab*", text)
print(x)