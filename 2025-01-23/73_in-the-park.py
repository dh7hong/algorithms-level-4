def solution(park, routes):
    # Find the starting position 'S'
    for i, row in enumerate(park):
        if 'S' in row:
            x, y = i, row.index('S')
            break
    
    # Movement directions
    direction_moves = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    
    # Process each command
    for route in routes:
        direction, steps = route.split()
        move_x, move_y = direction_moves[direction]
        temp_x, temp_y = x, y  # Temporary coordinates for simulation
        
        # Simulate movement and check validity
        for _ in range(int(steps)):
            temp_x, temp_y = temp_x + move_x, temp_y + move_y
            if not (0 <= temp_x < len(park) and 0 <= temp_y < len(park[0])) or park[temp_x][temp_y] == 'X':
                break
        else:
            x, y = temp_x, temp_y  # Update position if valid
    
    return [x, y]

# Test cases
print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))  # [2,1]
print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]))  # [0,1]
print(solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]))  # [0,0]
