import math

def encrypt(p, q, b, message):

    print("\np is '%s', q is '%s' and b is '%s'" % (p, q, b))

    bin1 = bin(p)
    bin2 = bin(q)

    bin1, bin2 = bin1[2:], bin2[2:]

    n = int(bin1, 2) * int(bin2, 2)
    
    phi = (int(bin1, 2) - 1) * (int(bin2, 2) - 1)

    check_relatively_prime(b, phi)

    print("\nThe public keys are 'n = %s' and 'b = %s'" % (n, b))

    a = multiplicative_inverse(b, phi)     # d is also used here instead of a 

    print("\nThe private keys are 'p = %s', 'q = %s' and 'a = %s'" % (p, q, a))

    check_congruence(a, b, phi)

    cipher = (message ** b) % n

    print("\nThe encryption of '%s' gives us '%s'" % (message, cipher))

    return n, a, cipher

def decrypt(cipher, a, n):
    decrypted = (square_and_multiply(cipher, a)) % n

    print("\nThe decryption of '%s' gives us '%s'" % (cipher, decrypted))
    return decrypted

def check_congruence(a, b, phi):
    if((a * b) % phi == 1):
        print("\n'a * b' IS congruent with '1 (mod (p-1)(q-1))'")

    else: 
        print("\n'a * b' is NOT congruent with '1 (mod (p-1)(q-1))'")

# Choose either of the multiplicative-inverse functions
def multiplicative_inverse(x, phi):
    a = pow(x, -1, phi)
    return a

def naive_multiplicative_inverse(a, n):
    for x in range(0, n - 1):
        if(((a * x) % n) == 1 % n):
            return x

def multiplicative_inverse_specific_power(x, power, n):
    a = pow(x, power, n)

    return a

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

def square_and_multiply(x, y):
    exp = bin(y)
    value = x
 
    for i in range(3, len(exp)):
      value = value * value
      if(exp[i:i + 1] == '1'):
        value = value * x
    return value

def sign_message(message, a, n):
    signed_message = (message ** a) % n
    print("\nThe signed message using this encrypt-system is: %s" % signed_message)
    return signed_message


def verify_message(x, y, n, b):
    res1 = multiplicative_inverse_specific_power(y, b, n)
    res2 = x % n

    if(res1 == res2):
        print("\nThe message (%s, %s) is most likely from Alice" % (x, y))
        return True

    else: 
        print("\nThe message (%s, %s) is NOT from Alice" % (x, y))
        return False


def main():

    p_alice = 13  
    q_alice = 19
    b_alice = 5  # e is also used here
    message = 30

    # Alice generates her RSA-system
    n_alice, a_alice, _, = encrypt(p_alice, q_alice, b_alice, message)
    
    # Alice signs a message to be sent to Bob with her own private key
    message_to_sign = 30
    signed_message = sign_message(message_to_sign, a_alice, n_alice)
    
    bob_p = 23
    bob_q = 19
    bob_b = 13

    # Bob generates his RSA-system
    n_bob, a_bob, _, = encrypt(bob_p, bob_q, bob_b, message)

    print("\nAlice encrypts the signed message with Bob's public key")
    _, _, signed_encrypted_message = encrypt(bob_p, bob_q, bob_b, signed_message)
    print("\nAlice encrypts the original message with Bob's public key")
    _, _, encrypted_message = encrypt(bob_p, bob_q, bob_b, message_to_sign)


    # Bob decrypts the signed and encrypted message from Alice with his own private key
    decrypted_signed_bob = decrypt(signed_encrypted_message, a_bob, n_bob)
    # Bob decrypts the original message from Alice with his own private key
    decrypted_original_bob = decrypt(encrypted_message, a_bob, n_bob)
   
    x, y = decrypted_signed_bob, decrypted_original_bob

    # Bob verifies that the message was sent from Alice with Alice's public key
    verify_message(y, x, n_alice, b_alice) 


if __name__ == '__main__':
	main()