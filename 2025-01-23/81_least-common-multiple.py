def gcd(a, b):
    """Computes the Greatest Common Divisor (GCD) using the Euclidean Algorithm."""
    while b:
        a, b = b, a % b  # Keep reducing until remainder is 0
    return a

def lcm(a, b):
    """Computes the Least Common Multiple (LCM) using GCD."""
    return (a * b) // gcd(a, b)  # LCM formula: (a * b) / GCD(a, b)

def solution(arr):
    """Finds the LCM of multiple numbers in an array without using reduce()."""
    result = arr[0]  # Start with the first number
    for num in arr[1:]:  # Iterate over the rest of the numbers
        result = lcm(result, num)  # Compute LCM iteratively
    return result

# Example test cases
print(solution([2, 6, 8, 14]))  # Output: 168
print(solution([1, 2, 3]))  # Output: 6