import random
import hashlib

n=9
p=1001

a=random.randint(5, 10)

b=random.randint(10,20)

A = (n**a) % p
B = (n**b) % p

print('n: ',n,' (a shared value), n: ',p, ' (a prime number)')

print('\nAlice calculates:')
print('a (Alice random): ',a)
print('Alice value (A): ',A,' (n^a) mod p')

print('\nBob calculates:')
print('b (Bob random): ',b)
print('Bob value (B): ',B,' (n^b) mod p')

print('\nAlice calculates:')
keyA=(B**a) % p
print('Key: ',keyA,' (B^a) mod p')
print('Key: ',hashlib.sha256(str(keyA).encode()).hexdigest())

print('\nBob calculates:')
keyB=(A**b) % p
print('Key: ',keyB,' (A^b) mod p')
print('Key: ',hashlib.sha256(str(keyB).encode()).hexdigest())