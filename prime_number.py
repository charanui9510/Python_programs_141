def isPrimeNumber(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i ==0:
                return False
            else:
                return True
print(isPrimeNumber(7))
print(isPrimeNumber(2))
print(isPrimeNumber(3))
print(isPrimeNumber(4))


