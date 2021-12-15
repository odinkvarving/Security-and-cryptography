import math
import string

def multiplicative_inverse_table(nFrom, nTo):

    unique_numbers = []
    for i in range(nFrom, nTo):
        for j in range(nFrom, nTo):

            if((j * i) % (nTo - 1) == 1 % (nTo - 1)):
                unique_numbers.append(math.gcd(j, i))
                 
    unique_numbers = set(unique_numbers)
    print(sorted(unique_numbers))

def naive_multiplicative_inverse(a, n):
    for x in range(0, n - 1):
        if(((a * x) % n) == 1 % n):
            print("\nMultiplicative inverse of %s modulo %s using naive-method results in: \n%s" % (a, n, x))

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def extended_multiplicative_inverse(a, n):
    gcd, x, y = egcd(a, n)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        print("\nMultiplicative inverse of %s modulo %s using extended EGCD results in: \n%s\n" % (a, n, (x % n)))
        return x % n

def multiplicative_inverse_specific_power(x, power, n):
    a = pow(x, power, n)

    print("\nMultiplicative inverse of %s^%s modulo %s results in: \n%s\n" % (x, power, a))
    return a
            
def main():
    print("Multiplicative inverses in multiplication table of 12 for modulo 12")
    multiplicative_inverse_table(1, 13)

    print("Multiplicative inverses in multiplication table of 11 for modulo 11")
    multiplicative_inverse_table(1, 12) 

    naive_multiplicative_inverse(11, 29)

    naive_multiplicative_inverse(7, 29)

    extended_multiplicative_inverse(7, 29)

    multiplicative_inverse_specific_power(3, -5, 59)
    

if __name__ == "__main__":
    main()