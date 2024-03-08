#S03 e1. Correct the error
def g(a, b):
    return a - b


def f(a, b, c, d):
    t0 = a + b - g(a, 0)
    t1 = g(c, d)

    # Check if the denominator (t1) is zero before performing the division
    if t1 != 0:
        t3 = 2 * (t0 / t1)
        result = t0 + 2 * t1 + t3 * t3
        return result
    else:
        print("Error: Division by zero is not allowed.")
        return None  # or return an appropriate value indicating an error


# -- Main program
print("Result 1: ", f(5, 2, 5, 0))
print("Result 2: ", f(0, 2, 3, 3))
print("Result 3: ", f(1, 3, 2, 3))
print("Result 4: ", f(1, 9, 22.0, 3))