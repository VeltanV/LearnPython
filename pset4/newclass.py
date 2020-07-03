def genPrimes():
    primes = []
    testNumber = 1
    isPrimal = True
    count = 0
    while True:
        testNumber += 1
        if primes:
            count = 0
            for primal in primes:

                if testNumber % primal == 0:
                    break
                else:
                    count += 1
                if(count == len(primes)):
                    primes.append(testNumber)
                    yield testNumber

        else:
            primes.append(testNumber)
            yield testNumber



num = genPrimes()
print(num.__next__())
print(num.__next__())
print(num.__next__())
print(num.__next__())
print(num.__next__())


