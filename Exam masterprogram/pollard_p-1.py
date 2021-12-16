import math
import sympy

from RSA import gcd

def simple_pollard(n):

    for b in range(0, 2 ** 32):  # The range at which B should run to can be adjusted (2^32 will find a quarter of all 64-bit factors and 1/27 of all 96-bit factors)

        A = (2 ** (math.factorial(b))) % n

        F = math.gcd(A - 1, n)

        if(F > 1):
            print("\n'%s' was one of the prime factors of '%s' found by using b = '%s'" % (F, n, b))
            return F

def simple_pollard_V2(n, b):
    a = 2
    for j in range(2, b+1):
        print("\na^j mod n => {}^{} mod {}: ".format(a, j, n))
        a = (a**j) % n
        print("a: ", a)

    d = gcd(a-1, n)

    if (d > 1 & d < n):
        print("gcd of a-1: {} and n: {} = ".format(a, n), d)
        print("{} is a prime factor of {}".format(d, n))
    else:
        print("No factors for n: {} and b: {}".format(n, b))
         
def find_factors(n):
   
    a = 2
   
    i = 2
   
    while(True):
   
        a = (a**i) % n
   
        d = math.gcd((a-1), n)
   
        if (d > 1):

            return d
      
        i += 1

def pollard(n):
    
    num = n
    
    ans = []

    while(True):
    
        d = find_factors(num)
    
        ans.append(d)
    
        r = int(num/d)
    
        if(sympy.isprime(r)):
    
            ans.append(r)
    
            break
    
        else:
    
            num = r
    
    print("\nPrime factors of", n, "are", *ans)

def main():

    n = 1829

    n2 = 6319

    # Can find prime factors of a number and which b was used to find it
    simple_pollard(n)
    simple_pollard(n2)  

    b = 7   
    # Can find prime factors of a number using a specific b, and prints the steps for finding it
    simple_pollard_V2(n2, b)
    
    pollard(18779)
    pollard(42583)

    

if __name__ == '__main__':
	main()