# alculating GCD or HCF


# Optimal Function for calculating GCD or HCF
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
    
# main function
if __name__ == '__main__':
    a = int(input())    
    b = int(input())
    print(gcd(a, b))