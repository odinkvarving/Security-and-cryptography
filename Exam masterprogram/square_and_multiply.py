
def exp_func(x, y):
    exp = bin(y)
    print ("Binary value of b is:", exp)
    print ("Bit\tResult")
    value = x
 
    for i in range(3, len(exp)):
      value = value * value
      print (i - 1, ":\t", value, "(square)")
      if(exp[i:i + 1] == '1'):
        value = value * x
      print (i - 1, ":\t", value, "(multiply)")
    return value

def main():

    a = 5
    b = 117
    p = 209

    print ("\nWe will calculate a^b")
    print ("a =", a)
    print ("b =", b)
    print ("==== Calculation ====")
    res = exp_func(a, b)
    print ("Result: ", res)

    modulus = res % p

    print("\nThe equation '%s^%s mod %s' results in: %s" % (a, b, p, modulus))

if __name__ == '__main__':
	main()