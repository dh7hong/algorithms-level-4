def solution(n):
    """Finds the number of ways to jump n steps using 1-step and 2-steps."""
    if n == 1:  # Base case for n=1
        return 1
    elif n == 2:  # Base case for n=2
        return 2
    
    # Create an array to store computed values
    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2
    
    # Compute ways iteratively
    for i in range(3, n + 1):
        ways[i] = (ways[i - 1] + ways[i - 2]) % 1234567  
        # Fibonacci relation with modulo
    
    return ways[n]  # Return the final computed value

# Example test cases
print(solution(4))  # Output: 5
print(solution(3))  # Output: 3
print(solution(10))  # Output: 89