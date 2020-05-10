# Amicable numbers are a pair of numbers, each of which is the sum of the factors of the other (e.g. 220 and 284).
# In the following Program, we will find pair of amicable numbers to a certain limit.
# For example, if we set the upper limit as 50000, then our preferred answer will be
# [[220, 284], [1184, 1210], [2620, 2924], [5020, 5564], [6232, 6368], [10744, 10856], [12285, 14595], [17296, 18416]]

ul = int(input(("Enter Upper Limit: ")))

def factors(n):
    flist = []
    for i in range(1,n+1):
        if n%i == 0:
            flist.append(i)
    return flist

def sumfact(n):
    nfact = factors(n)
    nlen = len(nfact)
    sum = 0
    for i in range(nlen-1):
        sum = sum + nfact[i]
    return sum


def is_amicable(a):
    b = sumfact(a)
    q = sumfact(b)
    if a == q and a != b:
        return True
    else:
        return False

def org_am_list(i):
    list1 = []
    if is_amicable(i):
        a = i
        b = sumfact(i)
        min = a if a < b else b
        max = a if a > b else b
        list1.append(min)
        list1.append(max)
        return list1


def am_upto(num):
    mainlist = []
    for i in range(num):
        a = org_am_list(i)
        if a not in mainlist:
            mainlist.append(a)
    return mainlist[1:]

print(am_upto(ul))
        
