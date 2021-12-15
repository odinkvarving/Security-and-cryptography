import random
import hashlib

n = 69
p = 419
a = 5
b = 8

a1 = (n**a) % p
b1 = (n**b) % p

print("\nAlice og Bob blir enige om et stort primtall 'p = %s' og et heltall 'n = %s'" % (p, n))

print("\nAlice kalkulerer 'n^a mod p = a1' og sender det til Bob")
print("Dette resulterer i '%s^%s mod %s = %s'" % (n, a, p, a1))

print("\nBob kalkulerer 'n^b mod p = b1' og sender det til Alice")
print("Dette resulterer i '%s^%s mod %s = %s" % (n, b, p, b1))

k1=(b1**a) % p
print("\nAlice beregner k = b1^a som resulterer i en felles nøkkel '%s'" % k1)
print('Hashet verdi (sha256): ',hashlib.sha256(str(k1).encode()).hexdigest())

k2=(a1**b) % p
print("\nBob beregner k = a1^a som resulterer i en felles nøkkel '%s'" % k2)
print('Hashet verdi (sha256): ',hashlib.sha256(str(k2).encode()).hexdigest())