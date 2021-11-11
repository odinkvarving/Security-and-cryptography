import math

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
            
            new_index = (m_indexes[counter] + c_indexes[j])
            
            if(new_index > 28):
                new_index -= 29
                encrypted_chars.append(new_index)

            else:    
                encrypted_chars.append((m_indexes[counter] + c_indexes[j])) 
            
            counter += 1

            if(counter == len(m_indexes)):
                break

    print("\nIndexes of encrypted characters: ", encrypted_chars)
    
    encryption = find_chars(encrypted_chars)
    
    string = "".join(encryption)
    
    print("Encrypted message: ", string.upper())

def decrypt(message, cipher):

    message = message.replace(" ", "").lower()

    encrypted_chars = []
                                                        
    m_indexes = find_indexes(message)
    c_indexes = find_indexes(cipher)

    counter = 0
    while(counter != len(m_indexes)):
        for j in range(len(cipher)):
            
            new_index = (m_indexes[counter] - c_indexes[j])
            
            if(new_index < 0):
                new_index += 29
                encrypted_chars.append(new_index)

            else:    
                encrypted_chars.append((m_indexes[counter] - c_indexes[j])) 
            
            counter += 1

            if(counter == len(m_indexes)):
                break

    print("\nIndexes of encrypted characters: ", encrypted_chars)
    
    encryption = find_chars(encrypted_chars)
    string = "".join(encryption)
    
    print("Decrypted message: ", string.lower())
    
def main():

    decrypt("LPÆLZJWKKBGYÅMFGWÆÆYYMBKVÆRYAÆFOFJGOMDDZIVGFÆØRXMYYRLZQÆIBXYÅÆYGKHSKLING", "elskling")
    
if __name__ == "__main__":
    main()