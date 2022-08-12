import re

p = re.compile("[a-zA-Z]")

finded = p.search("a4564fsddaAAA34FRG")
print(finded)
print(finded.group())