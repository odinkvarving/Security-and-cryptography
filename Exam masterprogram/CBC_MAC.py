x1 = '1101 1111 1010 0001'
x2 = '0010 1100 0001 1111'
IV = '0000'

def CBC_MAC(message):
    message = message.split()

    initial_binary = binary_xor(message[0], IV)
    e1 = hash(initial_binary)
    
    second_binary = binary_xor(e1, message[1])
    e2 = hash(second_binary)
   
    third_binary = binary_xor(e2, message[2])
    e3 = hash(third_binary)
    
    fourth_binary = binary_xor(e3, message[3])
    e4 = hash(fourth_binary)

    print("\nThe CBC-MAC for the message '%s' was: %s\n" % (''.join(message), e4))
    
def binary_xor(bin1, bin2):
    xored = int(bin1, 2) ^ int(bin2, 2)

    return bin(xored)

def hash(x):
    x = x[2:]
    hashed_binary = ((int(x, 2) + 3) % (2 ** 4))

    hashed_binary = bin(hashed_binary)[2:]

    x_length = len(str(x))

    hashed_string = str(hashed_binary)

    hashed_string_length = len(hashed_string)

    corrected_binary = ''

    corrected_x = ''
    
    if(x_length < 4):
        for i in range(4 - (x_length + 1)):
            corrected_x += '0'

        x_length = len(corrected_x + hashed_string)


    if(hashed_string_length < x_length):
         for i in range(x_length - hashed_string_length):
            corrected_binary += '0'

    result = corrected_binary + hashed_string

    print("Result after iteration: %s" % result)
    
    return result

def main():

    CBC_MAC(x1)
    CBC_MAC(x2)

if __name__ == '__main__':
	main()