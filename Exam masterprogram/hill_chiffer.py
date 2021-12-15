import numpy as np

ALPHABET = list("abcdefghijklmnopqrstuvwxyzæøå")


def alphabet_index(char):
    return ALPHABET.index(char)

def alphabet_char(index):
    for i in range(len(ALPHABET)):
        if(i == index):
            return ALPHABET[i]

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def matrix_mod_inv(matrix, modulus):

    det = int(np.round(np.linalg.det(matrix)))  # Step 1)
    det_inv = egcd(det, modulus)[1] % modulus  # Step 2)
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )  # Step 3)

    return matrix_modulus_inv

keyMatrix = [[0] * 3 for i in range(3)]
 
# Generate vector for the message
messageVector = [[0] for i in range(3)]
 
# Generate vector for the cipher
cipherMatrix = [[0] for i in range(3)]
 
# Following function generates the
# key matrix for the key string
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
 
# Following function encrypts the message
def encrypt(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] *
                                       messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 29
 
def HillCipher(message, key):
 
    # Get key matrix from the key string
    getKeyMatrix(key)
 
    # Generate vector for the message
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
 
    # Following function generates
    # the encrypted vector
    encrypt(messageVector)
 
    # Generate the encrypted text
    # from the encrypted vector
    cipher_text = []
    for i in range(3):
        cipher_text.append(chr(cipherMatrix[i][0] + 65))

    result_string = ''.join(cipher_text)
 
    # Finally print the ciphertext
    print("\nEncrypting the plaintext '%s' with the key '%s' results in cipher: \n%s" % (message, key, result_string))
    return result_string

def decrypt(cipher):
    Kinv = matrix_mod_inv(keyMatrix, 29)
    decrypted = ""
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(alphabet_index(letter.lower()))

    split_C = [
        cipher_in_numbers[i : i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))
    ]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % len(ALPHABET)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += alphabet_char(number)
    
    print("\nDecrypting the cipher '%s' results in the plaintext: \n%s" % (cipher, decrypted.upper()))
    return decrypted

# Driver Code
def main():

    #Important to use a matrix that corresponds to the number of letters in the message
    #ACT is 3 letters - requires a 3 x 3 matrix
    #The key should accordingly be of a length as to produce such a matrix

    message = "ACT"
 
    key = "GYBNQKURP"
 
    result = HillCipher(message, key)

    decrypt(result)
 
if __name__ == "__main__":
    main()