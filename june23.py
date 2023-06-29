# TO REVERSE A GIVEN LIST

# iplist = [12, 35, 9, 56, 24]
# iplist.reverse()
# print(iplist)

# ------------------------------------------

# TO SWAP FIRST AND LAST ELEMENT IN A LIST

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

mylist = [12, 35, 9, 56, 24]

# def swap_list(mylist):
#     mylist[0], mylist[-1] = mylist[-1], mylist[0]
#     return mylist


# print(swap_list(mylist))

# ------------------------------------------
# Python3 program to swap elements
# at given positions

# Swap function
# def swapPositions(list, pos1, pos2):

# 	# popping both the elements from list
# 	first_ele = list.pop(pos1)
# 	second_ele = list.pop(pos2-1)

# 	# inserting in each others positions
# 	list.insert(pos1, second_ele)
# 	list.insert(pos2, first_ele)

# 	return list

# # Driver function
# List = [23, 65, 19, 90]
# pos1, pos2 = 1, 3

# print(swapPositions(List, pos1-1, pos2-1))

# -----------------------------------------
# FIND MAXIMUM OF TWO NUMBERS


# def maximum(a, b):
#     if a >= b:
#         return a
#     else:
#         return b


# print(maximum(5, 9))

# ---------------------------------------
"""
Input: khokho
Output: The entered string is symmetrical
        The entered string is not palindrome

Input:amaama
Output: The entered string is symmetrical
        The entered string is palindrome
"""

# Python program to check whether the string is Symmetrical or Palindrome

import re

# amaama madam
# input_str = "madam"
# reversed_str = input_str[::-1]

# if input_str == reversed_str:
#     print("The entered string is palindrome")
# else:
#     print("The entered string is not palindrome")

# if re.match("^(\w+)\Z", input_str) and input_str == input_str[::-1]:
#     print("The entered string is symmetrical")
# else:
#     print("The entered string is not symmetrical")

# ------------------------------------------------------------
# Python code
# To reverse words in a given string

# string = "geeks quiz practice code"
# s = string.split()[::-1]
# l = []
# for i in s:
#     l.append(i)
# print(" ".join(l))

# ----------------------------------------------
# input : geeks    output: skeeg

# mystring = "geeks"

# s = list(mystring[::-1])

# l = []
# for i in s:
#     l.append(i)
# print(" ".join(l))


# --------------------------------------------------


def rev_sentence(sentence):
    # first split the string into words
    words = sentence.split(" ")

    # then reverse the split string list and join using space
    reverse_sentence = " ".join(reversed(words))

    # finally return the joined string
    return reverse_sentence


print(rev_sentence("damodar goud in peerzadiguda"))
