# implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3.
# If the "compressed" string would not become smaller than the original string, your method
# should return the original string. You can assume the string has only uppercase and lowercase letters(a-z).

def string_compression(string):
    converted_string = list()
    current_letter = string[0]
    current_count = 1
    for index in range(1, len(string)):
        if string[index] == current_letter:
            current_count += 1
        else:
            converted_string.append(current_letter)
            converted_string.append(str(current_count))
            current_letter = string[index]
            current_count = 1
    # need to include the last letters
    converted_string.append(current_letter)
    converted_string.append(str(current_count))

    compressed = ''.join(converted_string)
    if len(compressed) > len(string):
        return string
    return compressed


if __name__ == '__main__':
    print(string_compression('aabcccccaaa'))
