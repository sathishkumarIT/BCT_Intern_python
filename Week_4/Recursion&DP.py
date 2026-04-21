#recursion
# A function that calls itself is called a recursive function

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(6))

#Dynamic Programming
# Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems and storing the results of those subproblems to avoid redundant work.

#Memoization
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
print(fibonacci(10))

#Tabulation
#Bottom-up approach
def fibonacci(n):
    if n <= 1:
        return n
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]
