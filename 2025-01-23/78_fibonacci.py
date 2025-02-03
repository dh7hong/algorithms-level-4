def solution(n):
    # Modulo constant to prevent integer overflow
    MOD = 1234567
    
    # Base cases: Fibonacci sequence starts with 0 and 1
    fib = [0, 1] + [0] * (n - 1)  # Create an array of size n+1 with default values

    # Compute Fibonacci numbers iteratively to avoid recursion overhead
    for i in range(2, n + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD  
        # Use modulo to prevent large numbers

    return fib[n]  # Return the nth Fibonacci number mod 1234567

# Example test cases
print(solution(3))  # Expected output: 2
print(solution(5))  # Expected output: 5
print(solution(10)) # Expected output: 55
