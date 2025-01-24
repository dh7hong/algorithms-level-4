def solution(s):
    count = 0  # Number of substrings
    i = 0  # Pointer to traverse the string
    
    while i < len(s):
        x = s[i]  # First character of the substring
        count_x = 0  # Count of 'x' occurrences
        count_non_x = 0  # Count of other character occurrences
        
        # Move forward until counts of x and non-x are equal
        while i < len(s):
            if s[i] == x:
                count_x += 1
            else:
                count_non_x += 1
            
            i += 1  # Move to the next character
            
            # When counts match, break and start a new substring
            if count_x == count_non_x:
                break
        
        count += 1  # One substring is counted

    return count

print(solution("banana"))        # Output: 3
print(solution("abracadabra"))   # Output: 6
print(solution("aaabbaccccabba")) # Output: 3

def solution_recursive(s, count=0):
    if not s:  # Base case: If the string is empty, return the count
        return count

    x = s[0]  # First character
    count_x = 0  # Count of 'x' occurrences
    count_non_x = 0  # Count of other character occurrences

    # Find the first balanced substring
    for i in range(len(s)):
        if s[i] == x:
            count_x += 1
        else:
            count_non_x += 1
        
        # If counts are equal, break and process the remaining substring
        if count_x == count_non_x:
            return solution_recursive(s[i + 1:], count + 1)

    # If the loop finishes without breaking, it means the remaining part is one substring
    return count + 1

print(solution_recursive("banana"))        # Output: 3
print(solution_recursive("abracadabra"))   # Output: 6
print(solution_recursive("aaabbaccccabba")) # Output: 3
