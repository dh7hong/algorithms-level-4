def solution(N, A, B):
    round_count = 1  # Start counting rounds from 1
    
    # Continue the tournament until A and B meet
    while A != B:
        # Assign new numbers for the next round
        A = (A + 1) // 2
        B = (B + 1) // 2
        round_count += 1  # Increment round count
    
    return round_count - 1  
    # Adjust count since last increment happens after meeting

# Example test case
print(solution(8, 4, 7))  # Output: 3