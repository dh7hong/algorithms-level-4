# def is_valid_bracket_sequence(s):
#     """Checks if the given bracket string 
#     is a valid sequence using a stack."""
#     stack = []
#     bracket_map = {')': '(', ']': '[', '}': '{'}  
#     # Mapping of closing to opening brackets
    
#     for char in s:
#         if char in "({[":  
#         # If it's an opening bracket, push to stack
#             stack.append(char)
#         elif char in ")}]":  # If it's a closing bracket
#             if not stack or stack[-1] != bracket_map[char]: 
#             # Check if top of stack matches
#                 return False
#             stack.pop()  
#             # Remove the matched opening bracket
    
#     return len(stack) == 0  # Stack must be empty for a valid sequence

# def solution(s):
#     """Returns the number of valid 
#     bracket sequences after rotating s."""
#     valid_count = 0
#     n = len(s)
    
#     for i in range(n):
#         rotated_s = s[i:] + s[:i]  # Rotate left by i positions
#         if is_valid_bracket_sequence(rotated_s):  # Check if valid
#             valid_count += 1
    
#     return valid_count

# # Example test cases
# print(solution("[](){}"))  # Output: 3
# print(solution("}]()[{"))  # Output: 2
# print(solution("[)(]"))    # Output: 0
# print(solution("}}}"))     # Output: 0


def good_str(s):
    stack = []
    
    for char in s:
        if char == '(' or char == '[' or char == '{':  # Opening brackets
            stack.append(char)
        elif char == ')':  # Closing parenthesis
            if not stack or stack[-1] != '(':  # Check if top matches
                return False
            stack.pop()
        elif char == ']':  # Closing square bracket
            if not stack or stack[-1] != '[':
                return False
            stack.pop()
        elif char == '}':  # Closing curly bracket
            if not stack or stack[-1] != '{':
                return False
            stack.pop()

    return len(stack) == 0  # Stack must be empty for a valid sequence

def solution(s):
    cnt = 0
    for _ in range(len(s)):
        if good_str(s):  # Check if rotated version is valid
            cnt += 1
        s = s[1:] + s[0]  # Rotate left instead of right for consistency
    return cnt
