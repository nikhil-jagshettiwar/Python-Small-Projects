import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()
print(re.match(r'Love', data))
