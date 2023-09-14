# Write a method to replace all spaces in a string with '%20.'
# You may assume that string has sufficient space at the end to hold the additional characters,
# and that you are given the 'true' length of the string. (Note: If implementing in Java, plase use a
# character array so that you can perform this operation in place.)
# Example
# Input: "Mr John Smith      ", 13
# Output: "Mr%20John%20Smith"

def urlify(string, length):
    trimmed_string = string[:length]
    converted_string = list()
    for letter in trimmed_string:
        if letter == ' ':
            letter = '%20'
        converted_string.append(letter)
    return ''.join(converted_string)


def urlify_python_cheats(string, length):
    trimmed_string = string[:length]
    return trimmed_string.replace(' ', '%20')


if __name__ == '__main__':
    print(urlify('Mr John Smith    ', 13))
    print(urlify_python_cheats('Mr John Smith    ', 13))
