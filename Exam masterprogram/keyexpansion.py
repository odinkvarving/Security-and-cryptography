RCon = [0x00000000, 0x01000000, 0x02000000,
		0x04000000, 0x08000000, 0x10000000, 
		0x20000000, 0x40000000, 0x80000000, 
		0x1b000000, 0x36000000]

# ["2B", "28", "AB", "09"]
# ["7E", "AE", "F7", "CF"]
# ["15", "D2", "15", "4F"]
# ["16", "A6", "88", "3C"]


def KEYEXPANSION(key):

    w = [()]*44

    for i in range(0, 4):
         w[i] = (key[4 * i], key[4 * i + 1], key[4 * i + 2], key[4 * i + 3])

    for i in range(4, 44):

        temp = w[i - 1]
        word = w[i - 4]
         
        if i % 4 == 0:

            rotated_word = ROTWORD(temp)
            substituted_word = SUBWORD(rotated_word)
            rcon = RCon[int(i/4)]

            temp = HEX_XOR(substituted_word, hex(rcon)[2:])

        word = ''.join(word)
        temp = ''.join(temp)
        
        xored = HEX_XOR(word, temp)
        w[i] = (xored[:2], xored[2:4], xored[4:6], xored[6:8])
    
    return w

def ROTWORD(word):
	return word[1:] + word[:1]


def SUBWORD(w):
    return ''.join(w) 

def HEX_XOR(w1, w2):

    bin1 = hex_to_binary(w1)
    bin2 = hex_to_binary(w2)

    xored = int(bin1, 2) ^ int(bin2, 2)

    hexed = hex(xored)[2:]

    if(len(hexed) != 8):
        hexed = '0' + hexed

    return hexed

def hex_to_binary(hex):
    
    return bin(int(str(hex), 16))

def formatted_print(w):
	print("\n\nKeywords: \n")

	for i in range(len(w)):
		print("w" + str(i), "=", w[i][0], w[i][1], w[i][2], w[i][3])

def main():
    
    key = ["2B", "7E", "15", "16", "28", "AE", "D2", "A6", "AB", "F7", "15", "88", "09", "CF", "4F", "3C"]

    w = KEYEXPANSION(key)

    formatted_print(w)
    

if __name__ == '__main__':
	main()