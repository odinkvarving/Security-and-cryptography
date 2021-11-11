import numpy as np
from keyexpansion import HEX_XOR

def get_linear_array(array):
    array = np.array(array.split(" "))
    return array.reshape(4, int(len(array) / 4)).transpose()

def get_column(array, index):
    return array[:, index].reshape(array.shape[0], 1)

def get_row(array, index):
    return array[index, :].reshape(1, array.shape[1])

def word_xor(w1, w2):
    result = ""
    for i in range(4):
        result += (HEX_XOR(w1[i, 0], w2[i, 0])) + " "

    return get_linear_array(result.strip()).transpose()

def formatted_print(array):

    result = ""
    for index in range(array.shape[0]):
        result += ' '.join(array[:, index]) + " "
    
    return result

#############################################################################################################

def ADDROUNDKEY(word, key):

    # Empty array with the same shape as word-array
    result = np.empty((word.shape[0], 0), dtype=word.dtype)

    # For each column in word-array  - xor every element in word-array column with every element in key-array column
    for index in range(word.shape[0]):
        result = np.append(result, word_xor(get_column(word, index), get_column(key, index)), axis = 1)
    
    return result

def SUBBYTES(word):
    return word

def SHIFTROWS(word, encrypt = True):
    
    result = np.empty((0, word.shape[1]), dtype=word.dtype)

    if encrypt:
        multiplier = 1
    else:
        multiplier = -1

    for row_index in range(word.shape[0]):
        result = np.append(result, np.roll(get_row(word, row_index), multiplier * row_index, 1), axis=0)
    
    return result


def encrypt(message, key):

    print("Message to be encrypted: \n%s" % formatted_print(message))

    addRoundKey = ADDROUNDKEY(message, key)
    print("\nAfter ADDROUNDKEY: \n%s" % formatted_print(addRoundKey))

    subBytes = SUBBYTES(addRoundKey)
    print("\nAfter SUBBYTES(x) = x \n%s" % formatted_print(subBytes))

    shiftRows = SHIFTROWS(subBytes)
    print("\nAfter SHIFTROWS: \n%s" % formatted_print(shiftRows))

    return shiftRows

def decrypt(message, key):

    print("Message to be decrypted: \n%s" % formatted_print(message))
    
    shiftRows = SHIFTROWS(message, encrypt = False)
    print("\nAfter SHIFTROWS: \n%s" % formatted_print(shiftRows))

    subBytes = SUBBYTES(message)
    print("\nAfter SUBBYTES(x)⁻¹ = x \n%s" % formatted_print(subBytes))

    addRoundKey = ADDROUNDKEY(subBytes, key)
    print("\nAfter ADDROUNDKEY: \n%s" % formatted_print(addRoundKey))

    return addRoundKey


def main():
    
    message = get_linear_array("24 59 66 0c 99 da 9b 00 d6 55 fd 20 e9 ff 46 95")
    encrypted_message = get_linear_array("26 FA 83 E7 2D CD 5D B8 C4 DC EB 12 70 CF D6 1E")
    key = get_linear_array("67 71 35 c4 ff da e5 ff 1c 54 e1 fd 7f 2e 88 b7")

    encrypt(message, key)
    decrypt(encrypted_message, key)


if __name__ == '__main__':
	main()




