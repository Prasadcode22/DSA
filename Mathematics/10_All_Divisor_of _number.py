# Calculating ALl Divisors of number
# Naive Solution
def divisors(n):
    for i in range(1, n+1):
        if (n%i == 0):
            print (i)

# Optimal Solution
def divisors2(n):       # Theta(sqrt(n)) Time Complexity
    i = 1 
    while (i*i <= n):
        if (n%i == 0):
            print(i)
        i += 1
    while (i >= 1):
        if n % i == 0:
            print(n//i)
        i -= 1

# Main Function
if __name__ == '__main__':
    n = int(input('Enter the number :'))
    (divisors(n))
    (divisors2(n))