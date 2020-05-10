# A prime number is a positive integer greater than one, that has no positive integer factors except one and itself.
# Since we have already dealt with number of factors of a number, I'm thinking to implement this idea finding prime number.
# The prime number has the factor of 1 and itself.
# So, number of factors of a prime number is always 2. We will use this logic to find it.
# After that, we will find prime numbers upto a certain limit.

def factors(n):
    flist = []
    for i in range(1,n+1):
        if n%i == 0:
            flist.append(i)
    return flist

def numfact(num):
    fno = []
    for i in range(1,num+1):
        fno.append(len(factors(i)))
    return fno

def is_prime(m):
    q = len(factors(m))
    if q == 2:
        return True
    else:
        return False
        
 limit = int(input("Enter the limit: "))
 
 for q in range(limit):
    if is_prime(q):
        print(q)
