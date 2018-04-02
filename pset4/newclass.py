def genPrimes():
    primes = []
    testNumber = 1
    isPrimal = True
    count = 0
    while True:
        testNumber += 1
        if(len(primes) == 0):
            primes.append(testNumber)
            yield testNumber
        else:
            count = 0
            for primal in primes:

                if((testNumber % primal) != 0):
                    count += 1
                    pass
                else:
                    break
                if(count == len(primes)):
                    primes.append(testNumber)
                    yield testNumber



num = genPrimes()
print(num.__next__())
print(num.__next__())
print(num.__next__())
print(num.__next__())
print(num.__next__())


