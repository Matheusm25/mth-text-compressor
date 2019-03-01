# This file contains functions to open and save the files

import decompressor


# Function to complete the size of the binaries
def add_0s(binary_list):
    aux_list = binary_list
    for i in range(len(binary_list)):
        while len(aux_list[i]) != 8:
            aux_list[i] = '0' + aux_list[i]
    return aux_list


# Function to turn hexadecimal numbers to decimals
def hex_to_decimal(number):
    aux_dict = {
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }

    if number in aux_dict:
        return aux_dict[number]
    else:
        return int(number)


# Function to turn binary numbers to decimals
def binary_to_decimal(number):
    decimal = [1]
    result = int()
    for i in range(1, len(number)):
        decimal.append('')
        decimal[i] = decimal[i - 1] * 2

    for i in range(len(decimal)):
        if number[i] == '1':
            result += decimal[(len(number) - i - 1)]

    return result


# Function that receives a binary sequence and save in bytes in a file
def save_file(file_name, binary_str):
    # If the binary sequence is not multiple of 8 i'll add 1's in the beginning
    while len(binary_str) % 8 != 0:
        binary_str = '1' + binary_str

    # Split the binary sequence in 8 bits each to complete a Bytes
    binary_list = decompressor.list_generator(binary_str, 8)

    # Turn the binary words in integers
    int_list = list()
    for i in range(len(binary_list)):
        int_list.append(binary_to_decimal(binary_list[i]))

    # Turn the integers numbers in Bytes
    byte_list = list()
    for i in range(len(int_list)):
        byte_list.append(bytes([int_list[i]]))

    # Write the Bytes in the file
    file = open(file_name + '.mth', 'wb')
    for i in byte_list:
        file.write(i)

    file.close()


# Function to open the file .mth and return a binary sequence
def open_file(file):
    # Open the file and stores the Bytes (in hexadecimal) inside a string
    try:
        input_file = open(file, 'rb')
    except FileNotFoundError:
        print("The file can't be found or can't be open!")
        exit(0)

    hex_str = input_file.read()
    input_file.close()

    # Turn each hexadecimal number in decimal
    int_list = list()
    for i in range(len(hex_str)):
        int_list.append(hex_to_decimal(hex_str[i]))

    # Turn each decimal in binary
    binary_list = list()
    for i in int_list:
        binary_list.append(format(i, 'b'))

    # The first 8 bits could be extra 1's that the save_file function added, so i keep the amount of 1's and turn then
    # into 0 in the original list
    adds = binary_list[0].count('1')
    binary_list[0] = '0'

    # Equal the size of the binary words
    binary_list = add_0s(binary_list)

    # Turn list into string
    binary_str = str()
    for i in binary_list:
        binary_str += str(i)

    # Withdraw the additional 1's
    if adds > 0:
        for i in range(adds):
            binary_str = binary_str[1:]

    return binary_str
