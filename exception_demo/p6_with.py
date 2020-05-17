file1 = open('a.txt', encoding='utf8')
try:
    data = file1.read()
finally:
    file1.close()

with open('a.txt', encoding='utf8') as file2:
    data = file2.read()
