#S02 e1. Print the first 11th first numbers of the Fibonacci series

a = 0
b = 1
for i in range(11):
    print(a, end=" ")
    a = b
    b = a + b
