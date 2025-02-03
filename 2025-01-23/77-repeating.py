def solution(s):
    transformation_count = 0  # Count of binary transformations applied
    zero_count = 0  # Total count of removed '0's

    while s != "1":  # Repeat until the string becomes "1"
        zero_count += s.count('0')  # Count and accumulate the number of '0's in the current string
        s = s.replace('0', '')  # Remove all '0's from the string

        length = len(s)  # Find the length of the remaining string (only '1's left)
        s = bin(length)[2:]  # Convert the length to binary and update s

        transformation_count += 1  # Increment transformation count

    return [transformation_count, zero_count]  # Return the result as a list

# Example test cases
print(solution("110010101001"))  # Expected output: [3, 8]
print(solution("01110"))         # Expected output: [3, 3]
print(solution("1111111"))       # Expected output: [4, 1]