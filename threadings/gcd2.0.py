from math import gcd, sqrt


def eratosthenes(n):
    sieve = list(range(n + 1))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    for i in range(n):
        if 0 in sieve:
            sieve.remove(0)
    return sieve

def isPrime(n):
    i=2
    while i<int(sqrt(n)):
        if n%i==0:
            return False
        i+=1
    return True
# n=int(input())
n = 9971
print(eratosthenes(n))
if n % 2 == 0:
    print(str(n//2) + ' ' + str(n//2))
    exit(0)
memory = 1
n1=n
sieve = eratosthenes(n//2)
divs=[]
k=0
# print(sieve[k])
while n>0:
    if n%sieve[k]==0:
        n/=sieve[k]
        divs.append(sieve[k])
    else:
        k+=1
print()
print(divs)