import math
import sympy

from RSA import gcd

def simple_pollard(n, B, a):
    A = (a ** (math.factorial(B))) % n

    F = math.gcd(A - 1, n)

    if(F > 1):
        print("\n'%s' was one of the factors of '%s' found by using B = '%s'" % (F, n, B))
        return F

    else:
        print("\n'%s' was NOT one of the factors of '%s' found by using B = '%s'" % (F, n, B))
        return 0
         
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

    n1 = 1829
    B1 = 5
    a1 = 2

    n2 = 6319
    B2 = 7
    a2 = 2

    simple_pollard(n1, B1, a1)
    simple_pollard(n2, B2, a2)  
    
    pollard(18779)
    pollard(42583)

    

if __name__ == '__main__':
	main()