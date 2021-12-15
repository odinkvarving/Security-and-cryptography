import math

# n = pq

p = 233
q = 167
b = 3

def RSA(p, q, message):

    print("\np is '%s', q is '%s' and b is '%s'" % (p, q, b))

    bin1 = bin(p)
    bin2 = bin(q)

    bin1, bin2 = bin1[2:], bin2[2:]

    n = int(bin1, 2) * int(bin2, 2)
    
    phi = (int(bin1, 2) - 1) * (int(bin2, 2) - 1)

    check_relatively_prime(b, phi)

    a = multiplicative_inverse(b, phi)

    check_congruence(a, b, phi)

    get_public_keys(n, b)

    cipher = encrypt(message, n)
    decrypt(cipher, a, n)

def encrypt(message, n):
    encrypted = (message ** b) % n

    print("\nThe encryption of '%s' gives us '%s'" % (message, encrypted))
    return encrypted

def decrypt(cipher, a, n):
    decrypted = (cipher ** a) % n

    print("\nThe decryption of '%s' gives us '%s'" % (cipher, decrypted))
    return decrypted

def get_public_keys(n, b):
    public_key = []

    public_key.append(n)
    public_key.append(b)
    
    print("\nThe public keys are 'n = %s' and 'b = %s'" % (public_key[0], public_key[1]))
    

def check_congruence(a, b, phi):
    if((a * b) % phi == 1):
        print("\n'a * b' IS congruent with '1 (mod (p-1)(q-1))'")

    else: 
        print("\n'a * b' is NOT congruent with '1 (mod (p-1)(q-1))'")

# Choose either of the multiplicative-inverse functions
def multiplicative_inverse(x, phi):
    a = pow(x, -1, phi)

    print("\nThe private keys are 'p = %s', 'q = %s' and 'a = %s'" % (p, q, a))
    return a

def naive_multiplicative_inverse(a, n):
    for x in range(0, n - 1):
        if(((a * x) % n) == 1 % n):
            print("\nThe private keys are 'p = %s', 'q = %s' and 'a = %s'" % (p, q, x))
            return x

def gcd(a, b):
    t = 0

    while(b != 0):
        t = a
        a = b
        b = t % b
    return a

def check_relatively_prime(a, b):
    if(gcd(a, b) == 1):
        print("\n'%s' and '%s' are relatively prime" % (a, b))

    else: 
        print("\n'%s' and '%s' are not relatively prime" % (a, b))


def main():

    message = 42
    
    RSA(p, q, message)


if __name__ == '__main__':
	main()