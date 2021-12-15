import numpy as np

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "æ", "ø", "å"]

def substitution_function(i):
    return (11 * i - 5) % 29

def generate_substitutionchiffer():

    alphabet_to_chiffer = []

    for i in range(len(alphabet)):
        number = substitution_function(i)
        alphabet_to_chiffer.append(alphabet[number].upper())

    print(alphabet_to_chiffer)
    return alphabet_to_chiffer

def find_permutation():

    alphabet_to_numbered_chiffer = []

    for i in range(len(alphabet)):
        number = (11 * i - 5) % 29
        alphabet_to_numbered_chiffer.append(number)
    
    return alphabet_to_numbered_chiffer

def inversePermutation(arr, size):

    inverse = np.zeros(size)
    inverse_list = []
    
    for i in range(0, size - 1):
        y = arr[i]
        inverse[y] = i
    
    for i in range(len(inverse)):
        inverse_list.append(int(inverse[i]))
    
    print(inverse_list)

def encrypt_string(string, chiffer):
    letter_indexes = []
    encrypted_string = []

    for char in string:
        for i in range(len(alphabet)):
            if(char == alphabet[i]):
                letter_indexes.append(i)
        
    for i in range(len(letter_indexes)):
        encrypted_string.append(chiffer[letter_indexes[i]])
    
    result_string = ''.join(encrypted_string)
    print("\nEncrypting '%s' using the substitution-chiffer results in the cipher: \n%s" % (string ,result_string))

def decrypt_chiffer_string(string, chiffer):
    letter_indexes = []
    decrypted_string = []

    for char in string:
        for i in range(len(chiffer)):
            if(char == chiffer[i]):
                letter_indexes.append(i)
        
    for i in range(len(letter_indexes)):
        decrypted_string.append(alphabet[letter_indexes[i]])
    
    result_string = ''.join(decrypted_string)
    print("\nDecrypting the cipher-string '%s' gives us the plaintext:\n%s" % (string ,result_string))

def main():

    substitution_chiffer = generate_substitutionchiffer()

    permutation = find_permutation()

    size = len(permutation)

    print("\nThe permutated alphabet with the numbers for each index: ")
    print(permutation)

    print("\nInverse permutation of f as sequence: ")
    inversePermutation(permutation, size)

    encrypt_string("alice", substitution_chiffer)

    decrypt_chiffer_string("SIØPBE", substitution_chiffer)

if __name__ == "__main__":
    main()