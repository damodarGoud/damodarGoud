import re

emails = """
DamodarPulimamidi@gmail.com
damodar.pulimamidi@university.edu
damoda321pulimamidi@my-work.net
8.damodar.goud@gmail.com
"""

pattern = re.compile(r"[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)")

matches = pattern.finditer(emails)

for match in matches:
    print(match)

# ---------------------------------------
# import re

# regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"


# def check(email):
#     if re.fullmatch(regex, email):
#         print("Valid Email")
#     else:
#         print("Invalid Email")


# email = "121.ankitrai.326@comnpq.com"
# check(email)

# -------------------------------------------
