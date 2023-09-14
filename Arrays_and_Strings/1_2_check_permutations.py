# Given two strings, write a method to decide if one is a permutation of the other.

from collections import defaultdict


def deconstruct_string(string):
    letter_dict = defaultdict(int)
    for letter in string:
        letter_dict[letter] += 1

    return letter_dict


def check_permutation(string1, string2):
    string1_deconstructed = deconstruct_string(string1)
    string2_deconstructed = deconstruct_string(string2)

    for letter in string1_deconstructed.keys():
        if string1_deconstructed[letter] != string2_deconstructed[letter]:
            return False
    return True


if __name__ == '__main__':
    print(check_permutation('listen', 'silent'))
    print(check_permutation('triangle', 'integral'))
    print(check_permutation('debit card', 'bad credit'))
    print(check_permutation('not a permutation', 'hello world'))
