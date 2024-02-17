"""
def hi(n):
    if (n == 0):
        return
    print(n)
    hi(n-1)
hi(5)

"""
"""

# factorial in recursion

def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
    print(fact)
print(fact(5))

"""
 # sum 

def CalSum(n):
    if(n == 0):
        return 0
    return CalSum(n-1) + n

sum = CalSum(10)
print(sum)   