def factorial_calc(x):
    if x == 1:
        return x
    else:
        return x * factorial_calc(x - 1)


x = int(input("Please input the integer to get the factorial : "))
factorial = factorial_calc(x)
print("The factorial of this number is : " + str(factorial))