# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word of phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters. The palindrome does not need to be limited just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc...)

from collections import defaultdict


def palindrome_permutation(input):
    letters_dict = defaultdict(int)
    input = input.replace(' ', '')
    for letter in input.lower():
        letters_dict[letter] += 1

    odd_count = 0
    for letter in letters_dict.keys():
        if letters_dict[letter] % 2 == 1:
            odd_count += 1
        if odd_count > 1:
            return False
    return True


if __name__ == '__main__':
    print(palindrome_permutation('Tact Coa'))
    print(palindrome_permutation('no no'))
    print(palindrome_permutation('vicic'))
    print(palindrome_permutation('racecar'))
    print(palindrome_permutation('rac car'))
