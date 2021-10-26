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
    counter = 0
    for i in indexes:
        for j in range(len(alphabet)):
            counter = 0
            if(not i > len(alphabet)):
                if(i == j):
                    chars.append(alphabet[j].upper())
                    break
            else:

                while(counter != i):
                    for k in range(len(alphabet)):
                        
                        counter += 1
                        if(counter == i):
                            chars.append(alphabet[k + 1].upper())
                            break
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
            
            encrypted_chars.append((m_indexes[counter] + c_indexes[j])) 
            counter += 1

            if(counter == len(m_indexes)):
                break

    print("Indexes of encrypted characters: ", encrypted_chars)
    encryption = find_chars(encrypted_chars)
    print("Encrypted characters: ", encryption)
    
def main():

    #encrypt("fisk", "lat")
    encrypt("Snart helg", "torsk")
    

if __name__ == "__main__":
    main()

