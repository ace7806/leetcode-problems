def countPrimes(n):
    primes = [True]*n
    primes[0]=False
    primes[1]=False
    for i in range(2,n):
        if primes[i]:
            for j in range(2,n):
                if i*j >= n: break
                primes[i*j]=False
    
    return [i for i in range(len(primes)) if primes[i]]

print(countPrimes(3))
