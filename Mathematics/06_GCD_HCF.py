# alculating GCD or HCF
def gcd2(a,b):          # a = 9 , b = 6 >> (3, 6)
    while a != b:       # 9!= 6 >> 3 != 6  >> (a = b) 3=3
        if a>b:         # 9 > 6 
            a -= b      # a = 3
        else:           # 3 < 6
            b -= a      # b = 3
    return b            # return b >> i.e = 3


# Optimal Function for calculating GCD or HCF
def gcd(a, b):                # (a,b) = (9,6) >> (6,3) >> (3,0)
    if b == 0:                # b != 0  >> same  >> (3,0) here b == 0
        return a              #                                       >> return a >> i.e =3
    else:                     # (a > b)  >> same
        return gcd(b, a%b)    # recursive gcd(a = b, b = a%b ) >> recursive gcd(3, 0)
    
# main function
if __name__ == '__main__':
    a = int(input())    
    b = int(input())
    print(gcd(a, b))
    print(gcd2(a, b))