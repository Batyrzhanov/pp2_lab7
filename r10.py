import regex

f = open('row.txt', 'r', encoding='utf-8')
text = f.read()
x = regex.sub(r'([a-z0-9])([A-Z])', r'\1_\2', text)
print(x)