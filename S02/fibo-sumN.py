#S02 e3. Print the sum of the first X terms of the Fibonacci series
def fibosum(n):
    a = 0
    b = 1
    total = 0
    for i in range(n):
        total += a
        a = b
        b = a + b

print("Sum of the First 5 terms of the Fibonacci series:", fibosum(5))
print("Sum of the First 10 terms of the Fibonacci series:", fibosum(10))
