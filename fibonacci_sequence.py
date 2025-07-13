#Fibonacci Sequence


# 🧠 What is the Fibonacci Sequence?
#The Fibonacci sequence is a series of numbers where:
#0, 1, 1, 2, 3, 5, 8, 13, 21, ...

#Each number is the sum of the two preceding ones: F(n)=F(n−1)+F(n−2)

#✅ Goal - You want to write a program that returns
# the Fibonacci number at position n, or generates the
# first n Fibonacci numbers.

fibonacci_cache = {}

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)
    fibonacci_cache[n] = value
    return value

for n in range(1, 1001):
    print(n, ":", fibonacci(n))