from math import gcd, sqrt
n = 4


def isPrime(a):
    i = 2
    while i < int(sqrt(a)):
        if a % i == 0:
            return False
        i += 1
    return True


def divs(a):
    i=2
    while i<=a/2:
        if a%i==0:
            print(i,end=' ')
            a/=i
            i=2
        i+=1
    print(int(a),end=' ')


while n < 1000:
    if n % 2 == 0:
        print(str(n) + ' ' + str(n//2) + ' ' + str(n//2))
        n+=1
        continue
    a = max([(x, n-x) for x in range(1, n)], key=lambda x: gcd(*x))
    if (n % 3 != 0) and (n % 2 != 0) and (isPrime(n) == False):
        print(str(n) + ' ' + str(a[0]) + ' ' + str(a[1]) + ' ',end='')
        print('( ',end='')
        divs(n)
        print(')')

    n += 1