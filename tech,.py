# FIND 2ND LARGEST NUMBER IN A GIVEN LIST.

list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]

list2 = list(set(list1))
print(list2)
list2.sort()
print(list2)
print(list2[-2])

# -------------------------------------

# find how many times substring occured in mainstring

# main_str = "abobbobnnbobob"

# sub_str = "bob"

# start_index = 0
# count_er = 0

# for i in range(len(main_str)):
#     j = main_str.find(sub_str, start_index)
#     if j != -1:
#         start_index = j + 1
#         count_er += 1


# print("Numberof occurences of given word is: ", count_er)


# -------------------------------------
# Matching regex objects

# import re

# phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
# mo = phoneNumRegex.search("My number is 415-555-4242 india 12345456678")
# print("Phone number found: " + mo.group())

# -------------------------------------
