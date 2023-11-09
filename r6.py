import regex

f = open('row.txt', 'r', encoding='utf-8')
text = f.read()
x = regex.sub(r'[ ,.]', ':', text)
print(x)