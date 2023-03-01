# Palindrome Number

def is_palindrome(x):
    rev = 0
    temp = x
    while temp != 0 :
        id = temp%10
        rev = rev * 10 + id
        temp = temp // 10
    return rev == x

if __name__ == '__main__':
    x = int(input("Enter the value of palindrome x: "))
    print(f'{x} is palindrome !!',is_palindrome(x))

