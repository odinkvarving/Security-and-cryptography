import math
import string

def multiplicative_inverse(nFrom, nTo):

    unique_numbers = []
    for i in range(nFrom, nTo):
        for j in range(nFrom, nTo):

            if((j * i) % (nTo - 1) == 1 % (nTo - 1)):
                unique_numbers.append(math.gcd(j, i))
                 
    unique_numbers = set(unique_numbers)
    print(sorted(unique_numbers))

def multiplicative_inverse_specific(a, n):
    for x in range(0, n - 1):
        if(((a * x) % n) == 1 % n):
            print(x)
            

def main():
    print("Multiplicative inverses in multiplication table of 12 for modulo 12")
    multiplicative_inverse(1, 13)

    print("Multiplicative inverses in multiplication table of 11 for modulo 11")
    multiplicative_inverse(1, 12) 

    print("Multiplicative inverses of 11 modulo 29")
    multiplicative_inverse_specific(11, 29)


if __name__ == "__main__":
    main()