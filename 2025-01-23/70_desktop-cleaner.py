def solution(wallpaper):
    # Initialize variables for the smallest and largest positions
    min_row, max_row = 50, 0
    min_col, max_col = 50, 0

    # Loop through the 2D wallpaper grid
    for i in range(len(wallpaper)):  # Iterate through rows
        for j in range(len(wallpaper[i])):  # Iterate through columns
            if wallpaper[i][j] == "#":  # If a file is found
                # Update min and max row indices
                min_row = min(min_row, i)
                max_row = max(max_row, i)
                
                # Update min and max column indices
                min_col = min(min_col, j)
                max_col = max(max_col, j)

    # Return the smallest rectangle covering all `#` symbols
    return [min_row, min_col, max_row + 1, max_col + 1]

# Example test cases
print(solution([".#...", "..#..", "...#."]))  
# Output: [0, 1, 3, 4]
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))  
# Output: [1, 3, 5, 8]
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))  
# Output: [0, 0, 7, 9]
print(solution(["..", "#."]))  
# Output: [1, 0, 2, 1]

