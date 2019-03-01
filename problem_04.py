''' 
Project 04 - Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(num):
    '''
    (int) -> boolean
    
    Check if a given num is a palindrom (can be read the same backwards and
    forwards. If so, return True. Else, return False.
    
    >>> is_palindrome(9009)
    True
    >>> is_palindrome(2632)
    False
    '''

    #convert num to string, to allow comparison between digits
    test = str(num)
    
    #compare 1st half of string to 2nd half of string
    for i in range(0, len(test)//2):
        first = test[i]
        second = test[(len(test) - 1) - i]
        if (first != second):
            return False
    return True


def large_palindrome():
    num = 999
    #iterate 1st number if no palindrome found
    for i in range(0, num):
        #multiply all possible options of 2nd number to 1st number
        for i in range(0, num):
            product = num * (num - i)
            if is_palindrome(product):
                return product
    return False

print(large_palindrome())