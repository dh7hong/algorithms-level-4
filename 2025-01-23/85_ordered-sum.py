def solution(elements):
    n = len(elements)  # Get the length of the elements list
    ele_ext = elements * 2  
    # Double the list to simulate circular behavior
    set_sums = set()  # A set to store unique sums

    # Iterate over all possible subarray lengths
    for length in range(1, n + 1):  
        # Iterate over all possible starting indices
        for begin in range(n):
            subarr_sum = sum(ele_ext[begin:begin + length])  
            # Calculate subarray sum
            set_sums.add(subarr_sum)  # Store it in the set
    result = len(set_sums)  # Get the count of unique sums
    return result  # Return the count of unique sums

# Example usage:
elements = [7, 9, 1, 1, 4]
print(solution(elements))  # Output: 18