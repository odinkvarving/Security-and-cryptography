# Eksempel på oppgave kan være å finne alle logaritmene log α β i Z11
# Her må man manuelt endre a og b til den dekker alle kombinasjoner av beta 1-10 og alpha 2-10 (krysstabell med beta øverst og alpha på siden)


k = 10  # self-chosen integer value for number of exponents to test for (never needs to exceed p -1)
a = 6  # base
b = 3 # power
p = 41 # modulo

def multiplicative_inverse(x, power, phi):
    a = pow(x, power, phi)

    return a

def shanks_algorithm(k, a, b, p): 

    print("\nUsing Shanks algorithm to find an x that solves %s^x ≅ %s mod %s ..." % (a, b, p))

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
                print("\nFound two common values in the list: %s^%s ≅ %s and %s(%s)^%s ≅ %s" % (a, e, f, b, a, g, h))
                print("\nThese are congruent modulo %s and can be re-written to: %s^%s ≅ %s" % (p, a, result, f))

                return (e + (g * (-1)))
    

def main():

    shanks_algorithm(k, a, b, p)

if __name__ == '__main__':
	main()