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

    print("\nElGamal-system med primtall p = %s og ekvivalensen %s^%s ≅ %s (mod 29)\nHvor meldingen x = 4 og k = 3 \nGir resultatet: %s\n" % (p, alpha, a, beta, result))

    return result

def decrypt(first_result, second_result, a, p):

    first_step = (first_result ** a) % 29

    second_step = multiplicative_inverse(first_step, p)

    result = (second_step * second_result) % p

    print("Dekryptering av [%s, %s] gir oss: %s\n" % (first_result, second_result, result))

def multiplicative_inverse(a, n):
    for x in range(0, n - 1):
        if(((a * x) % n) == 1 % n):
            return x 


def main():

    result_buffer = encrypt(p, alpha, beta, k, x)

    decrypt(result_buffer[0], result_buffer[1], a, p) 

if __name__ == '__main__':
	main()
