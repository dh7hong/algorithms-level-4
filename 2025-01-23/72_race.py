def solution(players, callings):
    # Step 1: Create a dictionary to store 
    # each player's index for quick lookup
    player_positions = {}
    for i, player in enumerate(players):
        player_positions[player] = i
    

    # Step 2: Process each calling (each overtake)
    for player in callings:
        # Get the current index of the player being called
        index = player_positions[player]
        
        # Skip if the player is already in 1st place 
        # (not necessary due to constraints)
        if index == 0:
            continue
        
        # Get the player in front
        front_player = players[index - 1]
        
        # Swap positions in the players list
        players[index - 1], players[index] = players[index], players[index - 1]
        
        # Update the indices in the dictionary
        player_positions[player] -= 1
        player_positions[front_player] += 1
    
    return players  # Return the updated ranking after all overtakes

# Example usage
players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
result = solution(players, callings)
print(result)  # Expected Output: ["mumu", "kai", "mine", "soe", "poe"]

# def solution(players, callings):
#     # Step 1: Create a dictionary to store each player's index for quick lookup
#     player_positions = {}
#     for i, player in enumerate(players):
#         player_positions[player] = i
    
#     # Step 2: Process each calling (each overtake)
#     for player in callings:
#         # Get the current index of the player being called
#         index_before = player_positions[player]
        
#         # Identify the player ahead
#         front_player = players[index_before - 1]
        
#         # Swap the two players in the list
#         players[index_before - 1], players[index_before] = players[index_before], players[index_before - 1]
        
#         # Update the dictionary to reflect new positions
#         player_positions[player] -= 1
#         player_positions[front_player] += 1
    
#     return players  # Return the updated ranking after all overtakes

# # Test cases
# players = ["mumu", "soe", "poe", "kai", "mine"]
# callings = ["kai", "kai", "mine", "mine"]
# print(solution(players, callings))  # Expected Output: ["mumu", "kai", "mine", "soe", "poe"]
