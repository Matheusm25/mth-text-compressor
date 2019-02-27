import key_genarator
import file_functions


# A function to set all binary words to the same length
def match_size(binary_list, entropy):
    aux_list = list(binary_list)
    for i in range(len(aux_list)):
        aux_list[i] = str(aux_list[i])
        while len(aux_list[i]) != entropy:
            aux_list[i] = '0' + aux_list[i]

    return aux_list


# This function create a set of the binary words that i'll use to replace the characters
def binary_range(num):
    aux_set = set()
    for i in range(num):
        aux_set.add(format(i, 'b'))
    return aux_set


# The function receives a set of binary words and return a ordered list
def order_set_str(ord_set):
    aux_list = list(ord_set)

    # Transforms the String list and turn in integer

    for i in range(len(aux_list)):
        aux_list[i] = int(aux_list[i])

    # Sort the array with the binaries
    for i in range(len(aux_list)):
        for j in range(len(aux_list) - 1):
            if aux_list[i] < aux_list[j]:
                aux = aux_list[i]
                aux_list[i] = aux_list[j]
                aux_list[j] = aux
    return aux_list


# The function receives a set of characters and sort them
def order_set_char(ord_set):
    aux_list = list(ord_set)

    for i in range(len(aux_list)):
        for j in range(len(aux_list) - 1):
            if aux_list[i] < aux_list[j]:
                aux = aux_list[i]
                aux_list[i] = aux_list[j]
                aux_list[j] = aux
    return aux_list


def compress(file):
    # Opens the file
    try:
        input_file = open(file, 'r')
    except FileNotFoundError:
        print("The file can't be found or can't be open!")
        exit(0)

    input_name = str(file)
    input_name = input_name.split('.')[0]
    # Stores in a String
    input_str = input_file.read()

    # put each character on set
    input_set = set()
    for i in range(len(input_str)):
        input_set.add(input_str[i])
    # The number of possibilities is the set size
    possibilities = len(input_set)
    input_file.close()

    # I make a range of binary numbers according to the amount of possibilities and then transform into an
    # ordered list

    binary_set = binary_range(possibilities)
    binary_list = order_set_str(binary_set)
    # Calculate the entropy of compression
    entropy = len(str(binary_list[-1]))
    binary_list = match_size(binary_list, entropy)

    input_list = order_set_char(input_set)

    # Replace each character with a binary word

    output_str = input_str
    for i in range(len(binary_list)):
        output_str = output_str.replace(str(input_list[i]), binary_list[i])

    # Generate key for the decompressor know what each bit means

    key = key_genarator.key_generator(input_list)
    final_output = key + output_str

    print('Key to decompress: \n' + key)
    print('Compressed file: \n' + output_str)
    print('Full file: \n' + final_output)

    file_functions.save_file(input_name, final_output)

    print("\nThe file " + input_name + " was compressed without any errors!")
