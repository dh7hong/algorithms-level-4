def solution(n, left, right):
    result = []  # Initialize result list
    
    for index in range(left, right + 1):  
        row = index // n  # Calculate row index
        col = index % n   # Calculate column index
        result.append(max(row, col) + 1)  # Compute value
    
    return result  # Return the extracted portion

# Example usage:
print(solution(3, 2, 5))  # Output: [3,2,2,3]
print(solution(4, 7, 14))  # Output: [4,3,3,3,4,4,4,4]
