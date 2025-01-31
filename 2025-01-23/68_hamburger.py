def solution(ingredient):
    # Define the valid hamburger pattern as [1, 2, 3, 1]
    pattern = [1, 2, 3, 1]
    stack = []  # Stack to keep track of ingredients
    count = 0  # Count of packed hamburgers
    
    for item in ingredient: # ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
        # item = 2, stack = []              
        stack.append(item)  # Add the ingredient to the stack
        # stack = [2]
        
        # Check if the last four elements in the stack form a valid hamburger
        if stack[-4:] == pattern:
            count += 1  # Increase the count of packed hamburgers
            del stack[-4:]  # Remove the last four elements as they form a hamburger
    
    return count  # Return the total number of packed hamburgers

# Example test cases
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))  # Output: 2
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))  # Output: 0