def solution(arr1, arr2):
    # Get dimensions of input matrices
    rows_A, cols_A = len(arr1), len(arr1[0])  # Rows and columns of arr1
    _, cols_B = len(arr2), len(arr2[0])  # Rows and columns of arr2
    
    # Initialize the result matrix with zeros
    # Initialize an empty list to store the matrix
    result = []  

# Iterate through each row index
    for _ in range(rows_A):
    # Create a row with 'cols_B' zeros
      row = [0] * cols_B  
    # Append the row to the result matrix
      result.append(row)
    
    # Perform matrix multiplication
    for i in range(rows_A): 
    # Iterate over rows of arr1
        for j in range(cols_B):  
        # Iterate over columns of arr2
            for k in range(cols_A):  
            # Iterate over elements in row/column
                result[i][j] += arr1[i][k] * arr2[k][j]  
                # Multiply and accumulate

    return result  # Return the final matrix

# Example usage:
print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
# Output: [[15, 15], [15, 15], [15, 15]]

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
# Output: [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
