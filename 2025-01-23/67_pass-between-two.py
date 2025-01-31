def solution(s, skip, index):
    # Create a set of characters to skip for fast lookup
    skip_set = set(skip)
    
    # Initialize an empty list to store valid characters
    valid_chars = []
    
    # Iterate through all lowercase letters from 'a' to 'z'
    for i in range(ord('a'), ord('z') + 1):
        char = chr(i)  # Convert ASCII value to character
        if char not in skip_set:  # Check if character is not in skip set
            valid_chars.append(char)  # Add to valid characters list
    
    # Create a dictionary to map each valid character to its shifted character
    char_map = {}
    valid_length = len(valid_chars)
    
    for i, char in enumerate(valid_chars):
        # Find the new position by shifting `index` places forward (mod valid_length to wrap around)
        new_position = (i + index) % valid_length
        char_map[char] = valid_chars[new_position]
    
    # Transform the input string using the character map
    result = ''.join(char_map[c] for c in s)
    
    return result

# def solution(s, skip, index):
#     s_new = []  # List to store transformed characters
#     skip_set = set(skip)  # Convert skip string to a set for quick lookup
    
#     for ch in s:
#         i = 0
#         while i < index:
#             ch = chr((ord(ch) + 1 - ord('a')) % 26 + ord('a'))  # Shift character forward
#             if ch not in skip_set:  # Check if the character is not in skip set
#                 i += 1  # Only count valid shifts
#         s_new.append(ch)  # Append transformed character
    
#     return ''.join(s_new)  # Convert list to string and return

# Example test case
s = "aukks"
skip = "wbqd"
index = 5
print(solution(s, skip, index))  # Output: "happy"