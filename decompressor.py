import key_genarator
import compressor
import file_functions


# This function turns a list into String
def list_string(input_list):
    output_str = str()

    for i in range(len(input_list)):
        output_str += input_list[i]

    return output_str


# generates a list of binary words
def list_generator(entrada, entropy):
    output_list = list()
    i = 0
    while i < len(entrada):
        output_list.append(entrada[i: i + entropy])
        i += entropy

    return output_list


def generate_char_possibilities(key):
    # generates a list with the char possibilities
    char_list = key_genarator.char_list_generator()

    possibilities = list()

    # Taking all the chars that the 1's in the key represents

    for i in range(len(char_list)):  # talvez eu tenha que fazer range(8, len(char_list)) em
        if key[i] == '1':
            possibilities.append(char_list[i])

    return possibilities


def decompress(file):
    input_name = str(file).split('.')[0]

    # Stores in a String
    file_str = file_functions.open_file(file)
    key = file_str[0:255]
    input_str = file_str[255:]

    # Generates a list of characters that are in the file
    possibilities_list = generate_char_possibilities(key)

    # I make an ordered list of binaries that fit the characters
    binary_set = compressor.binary_range(len(possibilities_list))
    binary_list = compressor.order_set_str(binary_set)

    # Calculate the entropy of compression
    entropy = len(str(binary_list[-1]))
    binary_list = compressor.match_size(binary_list, entropy)

    # I split the input into a list where each item is a character
    output_list = list_generator(input_str, entropy)

    # Replace each binary word for the characters
    for i in range(len(possibilities_list)):
        while output_list.count(binary_list[i]) != 0:
            output_list[output_list.index(binary_list[i])] = possibilities_list[i]

    output = list_string(output_list)

    output_file = open(input_name + '.txt', 'w')
    output_file.write(output)
    output_file.close()

    print("\nThe file " + input_name + " was decompressed without any errors!")
