"""
re.sub() 
The ‘sub’ in the function stands for SubString, a certain regular expression pattern is searched in the given string(3rd parameter), and upon finding the substring pattern is replaced by repl(2nd parameter), count checks and maintains the number of times this occurs. 
"""
# re.sub(pattern, repl, string, count=0, flags=0)


import re

# Regular Expression pattern 'ub' matches the
# string at "Subject" and "Uber". As the CASE
# has been ignored, using Flag, 'ub' should
# match twice with the string Upon matching,
# 'ub' is replaced by '~*' in "Subject", and
# in "Uber", 'Ub' is replaced.

# print(re.sub("ub", "KKKK", "Subject has Uber booked already", flags=re.IGNORECASE))

# Consider the Case Sensitivity, 'Ub' in
# "Uber", will not be replaced.

# print(re.sub("ub", "~*", "Subject has Uber booked already"))

# # As count has been given value 1, the maximum
# # times replacement occurs is 1

# print(
#     re.sub("ub", "~*", "Subject has Uber booked already", count=1, flags=re.IGNORECASE)
# )

# # 'r' before the pattern denotes RE, \s is for
# # start and end of a String.
# print(re.sub(r"\sAND\s", " & ", "Baked Beans And Spam", flags=re.IGNORECASE))
# -------------------------

import re

# escape() returns a string with BackSlash '\',
# before every Non-Alphanumeric Character
# In 1st case only ' ', is not alphanumeric
# In 2nd case, ' ', caret '^', '-', '[]', '\'
# are not alphanumeric

# print(re.escape("This is Awesome even 1 AM"))
# print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))

# ---------------------------------------------------------

import re

# Lets use a regular expression to match a date string
# in the form of Month name followed by day number
myregex = r"([a-zA-Z]+) (\d+)"

match = re.search(myregex, "I was born on June 24")

if match != None:
    # We reach here when the expression "([a-zA-Z]+) (\d+)"
    # matches the date string.

    # This will print [14, 21), since it matches at index 14
    # and ends at 21.
    print("Match at index %s, %s" % (match.start(), match.end()))

    # We use group() method to get all the matches and
    # captured groups. The groups contain the matched values.
    # In particular:
    # match.group(0) always returns the fully matched string
    # match.group(1) match.group(2), ... return the capture
    # groups in order from left to right in the input string
    # match.group() is equivalent to match.group(0)

    # So this will print "June 24"
    print("Full match: %s" % (match.group(0)))

    # So this will print "June"
    print("Month: %s" % (match.group(1)))

    # So this will print "24"
    print("Day: %s" % (match.group(2)))

else:
    print("The regex pattern does not match.")
