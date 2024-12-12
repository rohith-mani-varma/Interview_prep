import math
number = 101

if number<=1:
    print("Not prime")
elif number ==2 or number ==3:
    print("Prime number")
elif number%2 ==0 or number %3 ==0:
    print("Not prime")
elif number > 3:
    for i in range(5, int(math.sqrt(number))+1):
        if number % i ==0:
            print("Not prime")
            break
        else:
            print("Prime Number")
            break















# elif number > 3:
#     for i in range(5, math.sqrt(number)):
