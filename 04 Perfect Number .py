# As we are dealing with factors of a number, let's find out the perfect numbers.
# Perfect number is a positive integer, which is equal to the sum of its proper divisors.

def factors(n):
    flist = []
    for i in range(1,n+1):
        if n%i == 0:
            flist.append(i)
    return flist

def is_perfect(number):
    flist = factors(number)
    sum = 0
    for i in range(len(flist)-1):
        sum = sum + flist[i]
    if sum == number:
        return True
    else:
        return False

i=1
while i>0:
    if is_perfect(i):
        print(i)
