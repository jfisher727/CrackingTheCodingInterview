# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit(or zero edits) away.

#Example
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

from collections import defaultdict


def deconstruct_string(string):
    letter_dict = defaultdict(int)
    for letter in string:
        letter_dict[letter] += 1

    return letter_dict


def one_away(string1, string2):
    # the strings are more than 1 character apart in length so they can't possibly be one edit away
    if abs(len(string1) - len(string2)) > 1:
        return False

    num_edits = 0
    string1_decon = deconstruct_string(string1)
    string2_decon = deconstruct_string(string2)

    for letter in string1_decon:
        current_edits = abs(string1_decon[letter] - string2_decon[letter])
        num_edits += current_edits
        if num_edits > 1:
            return False
    return True


if __name__ == '__main__':
    print(one_away('pale', 'ple'))
    print(one_away('pales', 'pale'))
    print(one_away('pale', 'bale'))
    print(one_away('pale', 'bake'))
