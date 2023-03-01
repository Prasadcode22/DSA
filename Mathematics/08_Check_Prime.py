# Calculating whether the given number is prime or not
# Naive Solution 
def prime_check(n):
    if n == 1:
        return False
    for i in range(2,n):    # O(n) Time Complexity "Worst Case"
        if n % i == 0 :     # O(1) for even number
            return False
    return True
    
# Optimal Solution
def prime_check2(n):       # O(sqrt(n))  Time complexity
    if n == 1 :
        return False
    i = 2 
    while (i*i <= n):
        if n % i == 0 or n % 2== 0:
            return False
    return True

# Super Optimal Solution  3x times more efficient
def prime_check3(n):
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

# main Function
if __name__ == '__main__':
    n = int(input())
    print (prime_check(n))
    print (prime_check2(n))
    print (prime_check3(n))