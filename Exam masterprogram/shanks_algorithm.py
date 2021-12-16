# Eksempel på oppgave kan være å finne alle logaritmene log α β i Z11
# Her må man manuelt endre a og b til den dekker alle kombinasjoner av beta 1-10 og alpha 2-10 (krysstabell med beta øverst og alpha på siden)
# Eksempel på en oppgave kan være å finne en x som løser a^x ≅ b mod p eller å finne log a b (mod p)

a = 11   # base
b = 16   # power
p = 29  # modulo

def multiplicative_inverse(x, power, phi):
    a = pow(x, power, phi)

    return a

def shanks_algorithm(a, b, p): 

    print("\nUsing Shanks algorithm to find an x that solves %s^x ≅ %s mod %s ..." % (a, b, p))

    for k in range(0, p - 1):
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

        if(x != -1):
            print("\nx = %s solves the DLP %s^x ≅ %s mod %s \nBecause %s^%s mod %s = %s" % (x, a, b, p, a, x, p, b))
            return x
                

def list_contains(list1, list2):

    for e, f in list1.items():
        for g, h in list2.items():
            if(f == h):

                result = (e + (g * (-1)))
                print("\nFound two common values in the lists: \n%s^%s ≅ %s from L1 and %s(%s)^%s ≅ %s from L2" % (a, e, f, b, a, g, h))
                print("\nThese are congruent modulo %s and can be re-written to: %s^%s ≅ %s" % (p, a, result, f))

                return (e + (g * (-1)))
    return -1
    

def main():

    shanks_algorithm(a, b, p)

if __name__ == '__main__':
	main()