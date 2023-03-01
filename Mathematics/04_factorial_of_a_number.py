# Calculating Factorisl of number

def fun(n):
    result = 1
    for i in range(2, n+1):
        result = result * i

    return result
# using recursive function
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
    
    
if __name__ == '__main__':
    x = int(input("Enter the number :"))
    print(f'The factorial of {x} is :',fun(x))
    print(f'The factorial of {x} is :',fact(x))
