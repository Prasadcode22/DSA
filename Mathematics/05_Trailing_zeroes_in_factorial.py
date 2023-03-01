# # calculating number of zerores in factorial of th number
# class Calcu:

#     def __init__(self, fact, trail) -> None:
#         self.fact = fact()
#         self.trail = trail()

#     def fact(n):
#         if n == 0 :
#             return 1 
#         else:
#             return n* fact(n -1)
        

#     def trail():




#    def __name__ == '__main__'
 
# this program has theta(n) time complexity 
def ZeroesCount(n):
    fact = 1 
    for i in range(2,n+1):
        fact = fact * i

    x = fact
    res = 0
    while (fact%10 == 0):
        res += 1
        fact = fact // 10
    return res, x

# lets define optimal function for the counting of trailing zeroes
def ZeroesCount2(n):
    res = 0
    i = 5 
    while i<=n :
        res = res + n//i
        i *= 5
    return res 


if __name__ == '__main__':
    n = int(input("Enter the value :"))
    print(ZeroesCount(n))
    print(ZeroesCount2(n))

