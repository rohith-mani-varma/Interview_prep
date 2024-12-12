def factorial(number):
    ans = 1
    while number>=1:
        ans= number*ans
        number = number-1
    return ans

print(factorial(515))

def sum_of_digits(number):
    ans = 0
    while number>0:
        ans = number%10 + ans
        number = number//10
    return ans
print(sum_of_digits(20))