import re

count = 0

pattern = re.compile("ab")

matcher = pattern.finditer("babnnabmmab")

for match in matcher:
    count += 1
    print(match)

print("number of occurences is : ", count)
# -------------------------------------------------
