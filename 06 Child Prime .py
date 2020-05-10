# Child Prime is such a prime number which can be obtained by summing up the square of the digit of its parent prime number.
# For example, 23 is a prime. If we calculate 2^2+3^2 = 4+9 = 13, which is also a prime no. then we call 13 as a child prime of 23.


ul = int(input("Enter Upper Limit: "))
gt = int(input("Generation Thresold :"))


def is_prime(m):
    q = len(factors(m))
    if q == 2:
        return True
    else:
        return False

def sep(num): 
    res = list(map(int, str(num))) 
    return res

def factors(n):
    flist = []
    for i in range(1,n+1):
        if n%i == 0:
            flist.append(i)
    return flist

def primesum(num):
    if is_prime(num):
        a = sep(num)
        sum = 0
        for i in range(len(a)):
            sum = sum + a[i]**2
        return sum

def generation(num):
    gen = [num]
    g = num
    q = 1
    while q > 0:
        if is_prime(primesum(g)):
            g = primesum(g)
            gen.append(g)
        else:
            q = q*(-1)
    return gen
            
for i in range(ul):
    if is_prime(i):
        pg = generation(i)
        gn = len(pg)
        if gn >= gt:
            print(pg)
