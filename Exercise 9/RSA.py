import math

# n = pq

p = 233
q = 167
e = 3

def RSA(p, q, message):

    print("\np is '%s', q is '%s' and e is '%s'" % (p, q, e))

    bin1 = bin(p)
    bin2 = bin(q)

    bin1, bin2 = bin1[2:], bin2[2:]

    n = int(bin1, 2) * int(bin2, 2)
    
    phi = (int(bin1, 2) - 1) * (int(bin2, 2) - 1)

    check_relatively_prime(e, phi)

    d = multiplicative_inverse(e, phi)

    check_congruence(d, e, phi)

    get_public_keys(n, e)

    cipher = encrypt(message, n)
    decrypt(cipher, d, n)

def encrypt(message, n):
    encrypted = (message ** e) % n

    print("\nThe encryption of '%s' gives us '%s'" % (message, encrypted))
    return encrypted

def decrypt(cipher, d, n):
    decrypted = (cipher ** d) % n

    print("\nThe decryption of '%s' gives us '%s'" % (cipher, decrypted))
    return decrypted

def get_public_keys(n, e):
    public_key = []

    public_key.append(n)
    public_key.append(e)
    
    print("\nThe public keys are '%s' and '%s'" % (public_key[0], public_key[1]))
    

def check_congruence(d, e, phi):
    if((d * e) % phi == 1):
        print("\n'd * e' IS congruent with '1 (mod (p-1)(q-1))'")

    else: 
        print("\n'd * e' is NOT congruent with '1 (mod (p-1)(q-1))'")

def multiplicative_inverse(x, phi):
    d = pow(x, -1, phi)

    print("\nThe private key is '%s'" % d)
    return d

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