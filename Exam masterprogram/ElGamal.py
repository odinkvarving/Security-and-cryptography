# ElGamal example:
# Sett opp et ElGamal-system vha primtallet p = 29 og ekvivalensen 11^8 ≅ 16 (mod 29)
# Krypter meldingen 4 med k = 3 og dekrypter igjen
                                                              
# Her er alpha = 11, beta = 16, a = 8, p = 29, x = 4 og k = 3

# Offentlig nøkkel: p = 29, alpha = 11, beta = 16
# Privat nøkkel:    p = 29, alpha = 11, a = 8

p = 19
alpha = 13
beta = 14
k = 6
x = 3
a = 5

def encrypt(p, alpha, beta, k, x):

    first_step = (alpha ** k) % p

    second_step = (beta ** k) % p

    third_step = x * second_step

    result = [first_step, third_step]

    print("\nElGamal-system med primtall p = %s og ekvivalensen %s^%s ≅ %s (mod %s)\nHvor meldingen x = %s og k = %s \n\nGir resultatet: %s" % (p, alpha, a, beta, p, x, k, result))

    return result

def decrypt(first_result, second_result, a, p):

    first_step = (first_result ** a)

    first_step_inverse = multiplicative_inverse(first_step, p)

    result = (second_result * first_step_inverse) % p

    print("\nHer er offentlig nøkkel 'p = %s', 'alpha = %s' og 'beta = %s' \nPrivat nøkkel er 'a = %s'" % (p, alpha, beta, a))

    print("\nDekryptering av [%s, %s] gir oss: %s\n" % (first_result, second_result, result))

def multiplicative_inverse(a, n):
    for x in range(0, n - 1):
        if(((a * x) % n) == 1 % n):
            return x 


def main():

    result_buffer = encrypt(p, alpha, beta, k, x)

    decrypt(result_buffer[0], result_buffer[1], a, p) 

if __name__ == '__main__':
	main()
