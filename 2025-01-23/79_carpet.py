def solution(brown, yellow):
    total_tiles = brown + yellow  # Total area of the carpet
    
    # Loop through possible heights 
    # (starting from 3, since brown >= 8 ensures min height 3)
    for height in range(3, total_tiles + 1):
        if total_tiles % height == 0:  # Width must be an integer
            width = total_tiles // height  # Calculate corresponding width
            
            # Ensure width is greater than or equal to height
            if width >= height:
                # Check if the yellow region matches the given yellow count
                if (width - 2) * (height - 2) == yellow:
                    return [width, height]  # Return width first, then height

# Example test cases
print(solution(10, 2))   # Expected output: [4, 3]
print(solution(8, 1))    # Expected output: [3, 3]
print(solution(24, 24))  # Expected output: [8, 6]
