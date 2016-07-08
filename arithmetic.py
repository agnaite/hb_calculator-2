def add(numlist):
    sum = 0
    for x in numlist:
        sum = sum + x
    return sum

def subtract(numlist):
    difference = numlist.pop(0)
    for x in numlist:
        difference = difference - x
    return difference

def multiply(numlist):
    product = 1
    for x in numlist:
        product *= x
    return product

def divide(numlist):
    product = numlist.pop(0)
    for x in numlist:
        product /= float(x)
    return product

def square(numlist):
    # Needs only one argument
    return numlist[0] * numlist[0]

def cube(numlist):
    # Needs only one argument
    return numlist[0] * numlist[0] * numlist[0]

def power(numlist):
    return numlist[0] ** numlist[1]  # ** = exponent operator


def mod(numlist):
    return numlist[0] % numlist[1]

