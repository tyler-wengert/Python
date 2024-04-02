def isPrime(num: int):

    for i in range(2, num - 1):
        if (num % i == 0):
            return False
    
    return True

def pFactors(number: int):

    neg = False
    if number < 0:
        neg = True
        clean = -number
    else:
        clean = number

    if (not isPrime(clean)):
        for i in range(2, clean - 1):
            if (isPrime(i)):
                if (clean % i == 0):
                    if neg:
                        neg = False
                        return [-i] + pFactors(int(clean / i))
                    return [i] + pFactors(int(clean / i))
    
    return [number]

factors = pFactors(int(input("Please input a number: ")))

print(factors)
