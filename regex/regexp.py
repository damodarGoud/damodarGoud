import re

text_to_search = """
abcdefghijklmnopqrstuvwxyz.
ABCDEFGHIJKLMNOPQRSTUVWXYZ
123456789
Ha Ha HaHa
Mr.Robinson
Mrs.Jane Doe
Mr.John Doe

123-565-5656
525.636.1234
525*636*7878
"""


sentence = "start a sentence and bring it to an end"

# pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d\d")

pattern = re.compile(r"\d{3}.\d{3}.\d{4}")

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

# print(text_to_search[1:4])

# with open("data.txt", "r", encoding="utf-8") as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)


myregex = r"([a-zA-Z]+) (\d+)"

matches = re.search(myregex, "born on June 25 2024")
