x = '1101 1111 1010 0001'
x_inverse = '0010 1100 0001 1111'
IV = '0000'

def caesar_cipher(message):
    message = message.split()   

    arr = []
    for i in range(len(message)):
        if(i == 0):
            initial_binary = binary_xor(message[i], IV)
            print("AFTER XOR: %s" % initial_binary)
            hashed_binary = hash(initial_binary)
            print("AFTER HASH: %s" % hashed_binary)
            

    
def binary_xor(bin1, bin2):
    print("FIRST BIN: %s" % bin1)
    print("SECOND BIN: %s" % bin2)
    xored = int(bin1) ^ int(bin2)

    print("XORED: %s" % xored)
    return xored

def hash(x):
    hashed_binary = ((int(x) + 3) % (2 ** 4))

    length = len(str(x))

    print(length)

    hashed_string = str(hashed_binary)
    if(len(str(hashed_binary)) < length):
         hashed_string.zfill(length)

    print("HASHED STRING: %s" % hashed_string)

def main():

    caesar_cipher(x)

if __name__ == '__main__':
	main()