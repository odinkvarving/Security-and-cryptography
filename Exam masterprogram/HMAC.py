ipad = '0011'
opad = '0101'

def HMAC(key, message):

    print("\nCalculating HMAC for given message... \n")
    
    inner_part = combine_function(key, ipad, message)
        
    outer_part = combine_function(key, opad, inner_part)
    
    result = center_squared(outer_part)

    print("\nHMAC for message '%s' results in: %s\n------------------------------------" % (message, result))
    
    return result

def center_squared(expression):
    return (int(expression) ** 2) % (2 ** 8)

def combine_function(key, binary_string, appended_binary):
    
    xored = binary_xor(key, binary_string)

    print("'%s' xor '%s' = %s" % (key, binary_string, xored))

    appended = append(xored, appended_binary)

    print("'%s' appended with '0b%s' = %s" % (xored, appended_binary, appended))

    squared = center_squared(appended)

    binary_squared = decimal_to_binary(squared)

    print("Center-sqaured of '%s' = %s" % (appended, binary_squared))

    middle_four = ''

    for position in range(2, 6):
        middle_four += binary_squared[position]

    print("Middle four decimals in binary = %s\n" % middle_four)
    return middle_four

def decimal_to_binary(decimal):
    return ''.join(bin(decimal)[2:])

def binary_xor(bin1, bin2):

    xored = int(bin1, 2) ^ int(bin2, 2)

    return bin(xored)


def append(binary, message):

    sliced_binary = binary[2:]

    stringified_binary, stringified_message = str(sliced_binary), str(message)

    appended_binary = stringified_binary + stringified_message

    binary = bin(int(appended_binary, 2))

    sliced_binary = binary[2:]

    return sliced_binary

def main():

    key = '1001'
    message = '0110'

    HMAC(key, message)
    
    HMAC(key, '0111')

if __name__ == '__main__':
	main()
