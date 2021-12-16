# ElGamal example:
# Sett opp et ElGamal-system vha primtallet p = 29 og ekvivalensen 11^8 ≅ 16 (mod 29)
# Krypter meldingen 4 med k = 3 og dekrypter igjen
                                                              
# Her er alpha = 11, beta = 16, a = 8, p = 29, x = 4 og k = 3

# Offentlig nøkkel: p = 29, alpha = 11, beta = 16
# Privat nøkkel:    p = 29, alpha = 11, a = 8

p = 29
alpha = 11
beta = 16
k = 3
x = 4
a = 8

def encrypt(p, alpha, beta, k, x):

    first_step = (alpha ** k) % p

    second_step = (beta ** k) % p

    third_step = x * second_step

    result = [first_step, third_step]

    print("\nElGamal-system med primtall p = %s og ekvivalensen %s^%s ≅ %s (mod %s)\nHvor meldingen x = %s og k = %s \n\nGir krypteringen: %s" % (p, alpha, a, beta, p, x, k, result))

    return result

def decrypt(first_result, second_result, a, p):

    first_step = (first_result ** a)

    first_step_inverse = multiplicative_inverse(first_step, p)

    result = (second_result * first_step_inverse) % p

    print("\nHer er offentlig nøkkel 'p = %s', 'alpha = %s' og 'beta = %s' \nPrivat nøkkel er 'a = %s'" % (p, alpha, beta, a))

    print("\nDekryptering av [%s, %s] gir oss: %s" % (first_result, second_result, result))

def multiplicative_inverse(a, n):
    for x in range(0, n - 1):
        if(((a * x) % n) == 1 % n):
            return x 

def multiplicative_inverse_specific_power(x, power, n):
    a = pow(x, power, n)

    return a

def sign_message(message, k):
    first = (a ** k) % p
    k_inverse = multiplicative_inverse_specific_power(k, -1, p)
    second = ((message - (a * first)) * k_inverse) % (p - 1)

    print("\nDen signerte meldingen med dette ElGamal-systemet er: (%s, %s)" % (first, second))
    return first, second

def verify_message(message, gamma, delta):
    res1 = ((beta ** gamma) * (gamma ** delta)) % p
    res2 = (alpha ** message) % p

    if(res1 == res2):
        print("\nMeldingen (%s, (%s, %s)) ble mest sannsynlig sent fra Bob" % (message, gamma, delta))

    else: 
        print("\nMeldingen (%s, (%s, %s)) ble IKKE sendt fra Bob" % (message, gamma, delta))


def main():

    result_buffer = encrypt(p, alpha, beta, k, x)

    decrypt(result_buffer[0], result_buffer[1], a, p) 

    message_to_sign = 365
    sign_message(message_to_sign, k)

    message_to_verify, gamma, delta = 365, 7, 6
    verify_message(message_to_verify, gamma, delta)

if __name__ == '__main__':
	main()
