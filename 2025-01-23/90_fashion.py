def solution(clothes):
    # Step 1: Create a dictionary to store clothing 
    # categories and their item counts
    clothes_dict = {}  

    for item, category in clothes:
        if category in clothes_dict:
            clothes_dict[category] += 1  
            # Increment count if category exists
        else:
            clothes_dict[category] = 1  
            # Initialize count if category is new

    # Step 2: Calculate the number of outfit combinations
    total_combinations = 1  
    # Start with 1 because we'll use multiplication

    for count in clothes_dict.values():
        total_combinations *= (count + 1)  
        # (number of items in category + 1 for "not wearing")

    return total_combinations - 1  
    # Subtract 1 to exclude the case where no clothes are worn

# Example Test Cases
print(solution([["yellow_hat", "headgear"], 
                ["blue_sunglasses", "eyewear"], 
                ["green_turban", "headgear"]]))  # Output: 5
print(solution([["crow_mask", "face"], 
                ["blue_sunglasses", "face"], 
                ["smoky_makeup", "face"]]))  # Output: 3
