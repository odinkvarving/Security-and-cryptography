ALPHABET = list("abcdefghijklmnopqrstuvwxyzæøå")

def alphabet_index(char):
    return ALPHABET.index(char)

def alphabet_char(index):
    for i in range(len(ALPHABET)):
        if(i == index):
            return ALPHABET[i]

def encrypt(message, k):
    original_message = message
    message = list(message)

    result = []
    counter = 0
    previous = []
    for idx in range(len(message)):
        if(idx == 0):
            res = (alphabet_index(message[idx]) + k) % len(ALPHABET)
            previous.append(alphabet_index(message[idx]))
            result.append(res)
        else:
            res = (alphabet_index(message[idx]) + previous[counter]) % len(ALPHABET)
            previous.append(alphabet_index(message[idx]))
            result.append(res)
            counter += 1 
        
    string_representation = []
    for res in result:
        string_representation.append(alphabet_char(res).upper())

    result_string = ''.join(string_representation)
    print("\nEncrypting message: '%s' with key '%s' results in cipher: \n%s" % (original_message, k, result_string))

def decrypt_numbers(encrypted_numbers, k):
    original_numbers = encrypted_numbers
    encrypted_numbers = [int(num) for num in encrypted_numbers.split(" ")]

    result = []
    counter = 0
    for idx in range(len(encrypted_numbers)):
        if(idx == 0):
            res = (encrypted_numbers[idx] - k) % len(ALPHABET)
            result.append(res)
        else:
            res = (encrypted_numbers[idx] - result[counter]) % len(ALPHABET)
            result.append(res)
            counter += 1

    string_representation = []
    for res in result:
        string_representation.append(alphabet_char(res))

    result_string = ''.join(string_representation)
    print("\nDecrypting ciphernumbers: '%s' with key '%s' results in plaintext: \n%s" % (original_numbers, k, result_string))

def decrypt_text(encrypted_text, k):
    original_text = encrypted_text
    encrypted_text = list(encrypted_text)

    result = []
    counter = 0
    for idx in range(len(encrypted_text)):
        if(idx == 0):
            res = (int(alphabet_index(encrypted_text[idx].lower()) - k)) % len(ALPHABET) 
            result.append(res)
        else:
            res = (int(alphabet_index(encrypted_text[idx].lower()) - result[counter])) % len(ALPHABET)
            result.append(res)
            counter += 1

    string_representation = []
    for res in result:
        string_representation.append(alphabet_char(res))

    result_string = ''.join(string_representation)
    print("\nDecrypting ciphertext: '%s' with key '%s' results in plaintext: \n%s" % (original_text, k, result_string))

def main():

    k = 17
    plaintext = "goddag"
    encrypt(plaintext, k)

    k2 = 21
    plaintext2 = "start"
    encrypt(plaintext2, k2)

    dec_k = 5
    encrypted_numbers = "23 08 23 12 21 02 04 03 17 13 19"
    decrypt_numbers(encrypted_numbers, dec_k)

    dec_k2 = 21
    encrypted_text2 = "ÆJVULO"
    decrypt_text(encrypted_text2, dec_k2)



    ### FIKS PRINT AV ENCRYPTING MESSAGE: 


if __name__ == '__main__':
	main()