def solution(k, tangerine):
    """Finds the minimum number of different tangerine sizes 
    needed to collect k tangerines."""
    
    # Step 1: Manually count occurrences of each size
    count_dict = {}
    for size in tangerine:
        if size in count_dict:
            count_dict[size] += 1
        else:
            count_dict[size] = 1

    # Step 2: Extract counts and sort in descending order
    sorted_counts = sorted(count_dict.values(), reverse=True)
    
    # Step 3: Pick the most frequent sizes first
    selected_count = 0  # Number of selected tangerines
    size_used = 0  # Number of different sizes used
    
    for freq in sorted_counts:
        selected_count += freq  # Add the most frequent size
        size_used += 1  # Increase distinct size count
        
        if selected_count >= k:  # Stop when we've picked at least k tangerines
            return size_used

# Example test cases
print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))  # Output: 3
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))  # Output: 2
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))  # Output: 1
