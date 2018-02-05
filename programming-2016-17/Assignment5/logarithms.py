import math

def log_add(a, b):
    '''Adds to numbers in their logarithmic transformtions.

    :param a: The first logarithmically transformed number.
    :param b: The second logarithmically transformed number.
    :return: The log-sum of the two numbers
    '''

    if a == -float("inf"):
        return b
    elif b == -float("inf"):
        return a
    elif a > b:
        return a + math.log1p(math.exp(b-a))
    else:
        return b + math.log1p(math.exp(a-b))

def log_add_list(list_of_numbers):
    '''Adds all the logarithmically transformed numbers in a list.

    :param list_of_numbers: A list of logarithmically transformed numbers.
    '''
    result = -float("inf")
    for number in list_of_numbers:
        result = log_add(number, result)

    return result

def log_subtract(a , b):
    '''Subtracts a logarithmically transformed number b from another such number a.

    :param a: The first logarithmically transformed number.
    :param b: The second logarithmically transformed number.
    :return: The log-difference between a and b
    '''

    if a == -float("inf"):
        return b
    elif b == -float("inf"):
        return a
    elif a > b:
        return a + math.log1p(-math.exp(b - a))
    else:
        return b + math.log1p(-math.exp(a-b))

def log_subtract_list(list_of_numbers):
    '''Subtracts all the logarithmically transformed numbers in a list from the first one.

    :param list_of_numbers: A list of logarithmically transformed numbers.
    '''

    result = list[0]
    for number in list_of_numbers[1:]:
        result = log_subtract(result, number)

    return result
