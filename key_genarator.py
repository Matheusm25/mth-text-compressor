# The is a sequence of 255 bits where the 1's are characters that are in the file and the 0's aren't


def char_list_generator():
    # Make a list of characters that can be in the file
    number_list = list(range(1, 256))
    char_list = list(number_list)

    for i in range(len(char_list)):
        char_list[i] = chr(number_list[i])

    return char_list


def key_generator(file_chars):
    char_list = char_list_generator()
    key = list(char_list)

    # I compare the lists to set up my key (1 for char in the file and 0 if not)
    for i in range(len(char_list)):
        if char_list[i] in file_chars:
            key[i] = 1
        else:
            key[i] = 0

    # Transform the list in string

    key_str = str()
    for i in range(len(key)):
        key_str += str(key[i])

    return key_str
