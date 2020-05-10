# In this program, we will visualize the number of factors of a number upto a certain range. 
# We will first get the result in a list format and then visualize the trend using matplotlib.pyplot

import matplotlib.pyplot as plt

limit = int(input("Enter upper limit: "))

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
    
print(numfact(limit))
plt.plot(numfact(limit))
plt.show()

# Here, I want to mention a few observations.
