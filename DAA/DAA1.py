# Iterative approach with dynamic programming
def fibonacci_iterative_dp(n):
    if n <= 1:
        return n
    fib = [0, 1]  # Initialize base cases
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

# Recursive approach with dynamic programming (Memoization)
def fibonacci_recursive_dp(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_recursive_dp(n - 1, memo) + fibonacci_recursive_dp(n - 2, memo)
    return memo[n]

# Get user input
try:
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        print(f"Iterative DP Fibonacci ({n}):", fibonacci_iterative_dp(n))
        print(f"Recursive DP Fibonacci ({n}):", fibonacci_recursive_dp(n))
except ValueError:
    print("Invalid input. Please enter an integer.")
