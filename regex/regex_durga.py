# import re

# count = 0
# mystr = '"hahahaaaaha"'
# pattern = re.compile("ha")

# matcher = pattern.finditer(mystr)
# for match in matcher:
#     count += 1
#     print(match.start(), "-->", match.end(), "<--", match.group())

# -----------------------------------
# import re

# p = re.compile("\w")
# print(p.findall("He said * in some_lang."))

# print("-------------------------------")

# p = re.compile("\w+")
# print(
#     p.findall(
#         "I went to him at 11 A.M., he \
# said *** in some_language."
#     )
# )

# print("-------------------------------")

# p = re.compile("\W")
# print(p.findall("he said *** in some_language."))

# ---------------------------------------------------
import re

# '*' replaces the no. of occurrence
# of a character.
p = re.compile("ab")
print(p.findall("ababbaabbb"))
print("------------------------------")

p1 = re.compile("ab*")
print(p1.findall("ababbaabbb"))
