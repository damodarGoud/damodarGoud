import re


text_to_search = """
Mr.Schafer
Mr.Robinson
Ms.Linda
Mrs.Laxmi
Mr.
"""

sentence = "start a sentence then bring it to an end"

pattern = re.compile(r"(Mr|Mrs|Ms)\.?\s[A-Z]\w* ")

matches = pattern.findall(text_to_search)

for match in matches:
    print(match)
