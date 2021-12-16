
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "æ", "ø", "å"]

def find_indexes(text):

    indexes = []
    for char in text:
        for i in range (len(alphabet)):

            if(char == alphabet[i]):
                indexes.append(i)

    return indexes

def find_chars(indexes):
    chars = []
    
    for i in indexes:
        for j in range(len(alphabet)):
            if(i == j):
                chars.append(alphabet[j].upper())
                break
                 
    return chars

def encrypt(message, cipher):

    message = message.replace(" ", "").lower()

    encrypted_chars = []
                                                        
    m_indexes = find_indexes(message)
    c_indexes = find_indexes(cipher)

    counter = 0
    while(counter != len(m_indexes)):
        for j in range(len(cipher)):
            
            new_index = (m_indexes[counter] + c_indexes[j]) % 29
            encrypted_chars.append(new_index)
            
            counter += 1

            if(counter == len(m_indexes)):
                break

    encryption = find_chars(encrypted_chars)
    
    string = "".join(encryption)
    
    print("\nEncryption of the cipher '%s' results in the encrypted message: %s" % (cipher, string.upper()))
    print("Indexes of encrypted characters: %s" % encrypted_chars)

    return string.upper()

def decrypt(cipher, key):

    cipher = cipher.replace(" ", "").lower()

    encrypted_chars = []
                                                        
    m_indexes = find_indexes(cipher)
    c_indexes = find_indexes(key)

    counter = 0
    while(counter != len(m_indexes)):
        for j in range(len(key)):
            
            new_index = (m_indexes[counter] - c_indexes[j]) % 29
            encrypted_chars.append(new_index)

            counter += 1

            if(counter == len(m_indexes)):
                break

    encryption = find_chars(encrypted_chars)
    string = "".join(encryption)
    
    print("\nThe decryption of the cipher '%s' results in the message: %s" % (cipher.upper(), string.lower()))
    print("Indexes of decrypted characters: %s" % encrypted_chars)
    
def main():

    encrypted = encrypt("nå er det snart helg", "torsk")
    decrypt(encrypted, "torsk")
    
    decrypt("QZQOBVCAFFKSDC", "brus")
    

if __name__ == "__main__":
    main()

