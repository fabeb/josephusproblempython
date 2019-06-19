###############################################################
#                                                             #
#        Author: https://github.com/gr0wnedhog                #
#           Recommended python version: 3.7                   #
#                                                             #     
#     My personal attempt at solving the Josephus problem     #
#              Have fun messing with my code!                 #
#                                                             #
#             No additional libraries required!               #
#                                                             #
###############################################################



n=64 #Number of Persons included (41 standard)

def getM(n):
    for x1 in range(1,n): #find next smaller power of 2
        if 2**x1 < n and 2**(x1+1) > n:
            m = 2**x1
    return m #variable m represents this smaller power of 2

def getL(n): #this function calculates L for the formula "2*L+1"
    return (n - getM(n))

def getWinner(n): #this function will output the survivor
    if n == 1: #special case for n=1
        return 1
    if n == 0: #special case for n=0
        return 0
    for x2 in range(1,n): #checking if n is a power of two (since this will give us 1 as an survivor)
        if n**(1/x2) == 2:  
            return 1
            break
    return (2 * getL(n) + 1)

print(getWinner(n))

