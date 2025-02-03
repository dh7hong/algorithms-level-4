def solution(s):
    # Split the input string into a list of strings (numbers)
    numbers = list(map(int, s.split()))
    
    # Find the minimum and maximum values from the list
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Return the result as a string in the format "(min) (max)"
    return f"{min_val} {max_val}"

# Example test cases
print(solution("1 2 3 4"))       # Expected output: "1 4"
print(solution("-1 -2 -3 -4"))   # Expected output: "-4 -1"
print(solution("-1 -1"))         # Expected output: "-1 -1"