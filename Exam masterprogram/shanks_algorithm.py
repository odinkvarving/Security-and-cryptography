from ElGamal import multiplicative_inverse


k = 5
a = 3
b = 19
p = 59


def multiplicative_inverse(x, power, phi):
    a = pow(x, power, phi)

    return a

def shanks_algorithm(k, a, b, p): 

    common_found = False
    
    first_list = {}
    for i in range(1, k):
        res = (a ** i) % p
        first_list[i] = res

    second_list = {}
    counter = -1
    for i in range(1, k):
        if(i == 1):
            res = multiplicative_inverse(a, -1, p)
            second_list[-1] = res
        
        else:
            temp = multiplicative_inverse(a, (k * counter), p)
            res = (b * temp) % p
            second_list[k * counter] = res
            counter -= 1
            
    x = list_contains(first_list, second_list)

    print("\nx = %s solves the DLP %s^x ≅ %s mod %s" % (x, a, b, p))
            

def list_contains(list1, list2):

    for e, f in list1.items():
        for g, h in list2.items():
            if(f == h):

                result = (e + (g * (-1)))
                print("\n%s^%s ≅ %s and %s(%s)^%s ≅ %s" % (a, e, f, b, a, g, h))
                print("\nThese are congruent modulo %s and can be re-written to: %s^%s ≅ %s" % (p, a, result, f))

                return (e + (g * (-1)))
    

def main():

    shanks_algorithm(k, a, b, p)

if __name__ == '__main__':
	main()