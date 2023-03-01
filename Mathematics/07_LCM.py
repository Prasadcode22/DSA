# calculating LCM of Two Numbers
def lcm(a,b):
    res = max (a,b)
    while True:
        if res % a == 0 and res % b == 0 :
            return res
        res += 1
    return res


#  Optimal Solution
                              # using formulae a*b = gcd * lcm
def gcd(a,b):                 # >> O(log min(a,b)) Time Complexity
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
    
def lcm2(a,b):
    return a*b // gcd(a,b)

if __name__ == '__main__':
    a = int(input()) 
    b = int(input()) 
    print(lcm(a,b))
    print(lcm2(a,b))