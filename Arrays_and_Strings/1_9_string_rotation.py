# Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.
# eg., "waterbottle" is a rotation of "erbottlewat")

# NOTES
# rotation would mean that some letters from the end of the string are now at the beginning
# of the string.
# All but 1 of the letters coule be rotated from the end to the beginning
# waterbottle -> aterbottlew
# waterbottle -> terbottlewa
# waterbottle -> erbottlewat
# waterbottle -> rbottlewate
# waterbottle -> bottlewater
# waterbottle -> ottlewaterb
# waterbottle -> ttlewaterbo
# waterbottle -> tlewaterbot
# waterbottle -> lewaterbott
# waterbottle -> ewaterbottl

from collections import defaultdict


def deconstruct_string(string):
    letter_dict = defaultdict(int)
    for letter in string:
        letter_dict[letter] += 1

    return letter_dict


def is_substring(s1, s2):
    return s2 in s1


def string_rotation(s1, s2):
    return is_substring(s1+s1, s2)


if __name__ == '__main__':
    print(string_rotation('watterbottle', 'erbottlewat'))
