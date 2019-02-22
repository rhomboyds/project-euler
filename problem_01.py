'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def sum_multiples(num):
    '''
    (int) -> int

    Returns the sum of all multiples of 3 or 5 below num.

    >>> sum_multiples(10)
    23
    '''

    total = 0

    for i in range(0,num):
        #check if i is a multiple of 3 or 5
        if (i % 3 == 0) or (i % 5 == 0):
            total += i
    return total

print(sum_multiples(1000))
