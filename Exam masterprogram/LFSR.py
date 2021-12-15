def LFSR1(K_string):
    
    binary_string = K_string
    
    binary = [K_string]
    
    unfinished = True

    counter = 0
    
    while(unfinished):
        
        modified_list = [int(i) for element in binary for i in element]
        
        first_xor = to_binary(modified_list[:1]) ^ to_binary(modified_list[1:2])
        second_xor = first_xor ^ to_binary(modified_list[2:3])
        third_xor = second_xor ^ to_binary(modified_list[3:4])

        binary_string += str(third_xor)

        binary[0] = binary_string
        
        new_list = left_shift(binary)

        binary[0] = new_list

        binary_string = binary[0]

        counter += 1

        if(binary[0] == K_string):
            print("LFSR finished in %s periods with K = %s" % (counter, K_string))
            unfinished = False

def LFSR2(K_string):
    
    binary_string = K_string
    
    binary = [K_string]
    
    unfinished = True

    counter = 0
    
    while(unfinished):
        
        modified_list = [int(i) for element in binary for i in element]
        
        first_xor = to_binary(modified_list[:1]) ^ to_binary(modified_list[3:4])

        binary_string += str(first_xor)

        binary[0] = binary_string
        
        new_list = left_shift(binary)

        binary[0] = new_list

        binary_string = binary[0]

        counter += 1

        if(binary[0] == K_string):
            print("LFSR finished in %s periods with K = %s" % (counter, K_string))
            unfinished = False


def to_binary(element):
    binary_representation = ''.join(str(element))

    disallowed_characters = "[]"
    for character in disallowed_characters:
        binary_representation = binary_representation.replace(character, "")
    
    bin = int(binary_representation, 16)
    
    return bin

def left_shift(list):
    string = list[0]
    new_list = (string[1:])

    return new_list

def main():
    print("LFSR with Zi+4 = Zi + Zi+1 + Zi+2 + Zi+3 (mod 2): ")
    LFSR1("1000")
    LFSR1("0011")
    LFSR1("1111")
    
    print("\nLFSR with Zi+4 = Zi + Zi+3 (mod 2): ")
    
    LFSR2("1000")
    LFSR2("0011")
    LFSR2("1111")

if __name__ == '__main__':
	main()
