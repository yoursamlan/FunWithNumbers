#In this program we will enter a number and get its factors as the output in a list format.
num = int(input("Enter number: "))
def factors(n):
    flist = []
    for i in range(1,n+1):
        if n%i == 0:
            flist.append(i)
    return flist
print(factors(num))
