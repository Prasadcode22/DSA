# Check whether the factor is prime
def prime_check(n):
    if n == 1:
        return False
    if n == 2 or n ==3 :
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while(i*i <= n):
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True


# Calculating Prime Factorization of the given number
def prime_fact(n):
    print("Enter the Prime Factors is/are :")
    for i in range (2, n+1):
        if prime_check(i):
            x = i 
            while n%x == 0:
                print(i)
                x *= i                    
# Main Function               
if __name__ == '__main__':
    n = int(input("Enter the value for Prime Factorization :"))
    (prime_fact(n))
