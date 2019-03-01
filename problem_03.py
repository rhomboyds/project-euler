'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''




n = 600851475143
i = 2
while i * i <= n:
    while n % i == 0:
        n = n / i
    i = i + 1
print(n)














#def is_prime(num):
    #'''
    #(int) -> boolean

    #Returns True if num is a prime number. Else, returns False.

    #>>> is_prime(4):
    #False
    #>>> is_prime(5):
    #True
    #'''

    ##iterate all numbers up to num, excluding 1
    #for i in range(2, num):
        ##if any i is a factor of num, then it is not a prime number
        #if (num % i == 0):
            #return False
    ##no factors found in all number of loop means num is prime
    #return True


#def largest_prime(num):
    #'''
    #(int) -> int

    #Returns the largest prime factor of num.

    #>>> large_prime(13195)
    #29
    #'''

    ##for efficiency, start with the largest factor (num // 2), and work
    ##backwards to find the largest prime factor
    #for i in range(num // 2, 2, -1):
        #if (num % i == 0):
            #if (is_prime(i)):
                #return i
            #else:
                #print(i, '= not prime factor')
        #else:
            #print(i, '= not factor')

#print(largest_prime(600851475143))

















       
