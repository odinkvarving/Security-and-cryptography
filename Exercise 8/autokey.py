ALPHABET = list("abcdefghijklmnopqrstuvwxyzæøå")

def alphabet_index(char):
    return ALPHABET.index(char)

def encrypt(message, key_arr):
    
    message = list(message)
    keyword = list([ALPHABET[digit] for digit in key_arr])
    key = (list(keyword) + message)[:len(message)]

    result = []
    for idx in range(len(message)):

        res = alphabet_index(message[idx]) + alphabet_index(key[idx]) % len(ALPHABET)
        for i in range(len(ALPHABET)):
            if(res == i):
                char = ALPHABET[i]
                result.append(char.upper()) 
        
    result_string = ' '.join(result)
    return result_string

def decrypt(encrypted_message, key_arr):

    encrypted_message = [int(num) for num in encrypted_message.split(" ")]

    result = []
    for idx in range(len(encrypted_message)):
        
        res = encrypted_message[idx] - key_arr[idx] % len(ALPHABET)
        key_arr.append(res)
        result.append(ALPHABET[res])

    result = ''.join(result)
    return result    


def main():

    key_arr = [17]
    plaintext = "goddag"
    result = encrypt(plaintext, key_arr)

    print("Encrypting plaintext: '%s' with key: %s results in ciphertext: \n%s" % (plaintext, key_arr, result))

    dec_key_arr = [5]
    encrypted_text = "23 08 23 12 21 02 04 03 17 13 19"
    result = decrypt(encrypted_text, dec_key_arr)

    print("\nDecrypting message: '%s' with key: %s results in plaintext: \n%s" % (encrypted_text, [5], result))

if __name__ == '__main__':
	main()