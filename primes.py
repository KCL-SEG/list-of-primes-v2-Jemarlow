def isPrime(n):
    if (n < 2):
        return False
    elif (n == 2):
        return True
    else:

        for i in range(2, n):
            isPrime = n % i != 0

            if (isPrime is False):
                break

        if isPrime:
            return True
            



def primes(number_of_primes):

    if (number_of_primes <= 0):
        raise ValueError("Provided argument must be greater than zero.")

    list = []
    n = 0
    primesFound = 0

    while (primesFound < number_of_primes):
        if (isPrime(n)):
            list.append(n)
            primesFound += 1

        n += 1

    return list