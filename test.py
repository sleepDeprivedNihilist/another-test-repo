print("Hello World")

#recursion
def factorial(n):
    if n == 0 or n == 1: return 1
    else: return factorial(n-1)