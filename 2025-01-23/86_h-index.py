def solution(citations):
    citations.sort(reverse=True)  
    # Sort the citations in descending order
    h_index = 0  
    # Initialize H-Index

    # Iterate over the sorted list
    for i, citation in enumerate(citations):
        if citation >= i + 1:  
        # Check if at least (i+1) papers have (i+1) or more citations
            h_index = i + 1  
            # Update the H-Index
        else:
            break  # Stop when the condition fails

    return h_index  # Return the final H-Index

# Example usage:
citations = [3, 0, 6, 1, 5]
print(solution(citations))  # Output: 3