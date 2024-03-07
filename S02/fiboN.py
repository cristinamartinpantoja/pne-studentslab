#S02 e2. Print the th number of the Fibonacci list

def fibon(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return fibon(n - 1) + fibon(n - 2)

print("5th Fibonacci term:", fibon(5))
print("10th Fibonacci term:", fibon(10))
print("15th Fibonacci term:", fibon(15))




