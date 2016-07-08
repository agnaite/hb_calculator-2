def add(numlist):
    sum = reduce (lambda x, y: x + y, numlist)
    return sum

def subtract(numlist):
    difference = reduce (lambda x, y: x - y, numlist)
    return difference

def multiply(numlist):
    product = reduce (lambda x, y: x * y, numlist)
    return product

def divide(numlist):
    quotient = reduce (lambda x, y: x / y, numlist)
    return quotient

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

