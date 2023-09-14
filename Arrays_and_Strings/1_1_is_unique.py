# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# should return true if all the characters in the string are unique
# should return false if there are any duplicate characters
def is_unique(string):
    character_set = set()
    for letter in string:
        before_add = len(character_set)
        character_set.add(letter)
        after_add = len(character_set)

        if before_add == after_add:
            return False
    return True


def is_unique_no_extras(string):
    for i in range(0, len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True


if __name__ == '__main__':
    print(is_unique('abcdefghi'))
    print(is_unique('abcdefgai'))
    print('No extra data structure')
    print(is_unique_no_extras('abcdefghi'))
    print(is_unique_no_extras('abcdefgai'))
