def isPrime(n):
    for i in range(2, n):
        if n%i==0:
            return False
        return True
    
inputValue = isPrime(27)
print(inputValue)