# calculating number od digits in a given number

x = int(input('Enter the value of x:'))
result = 0
while x>0:
    x = x//10
    result += 1
print('The no of digit is/are :',result)

