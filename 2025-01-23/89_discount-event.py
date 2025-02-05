def solution(want, number, discount):
    # Step 1: Create a dictionary to store required items and their quantities
    required_items = {}  # This will store { item: required_quantity }
    for i in range(len(want)):
        required_items[want[i]] = number[i]  # Assign each item with its required quantity

    valid_start_days = 0  
    # Counter to track valid membership start days
    total_days = len(discount)  
    # Total days of available discounts

    # Step 2: Use a sliding window to check every possible 10-day period
    for start in range(total_days - 9):  
      # Ensure we get full 10-day windows
        window_items = {}  
        # Dictionary to store the count of items in the current 10-day window

        # Step 3: Count occurrences of each item in the 10-day window
        for i in range(start, start + 10):  
          # Check 10 consecutive days from 'start'
            item = discount[i]  
            # Get the item being discounted on that day
            if item in window_items:
                window_items[item] += 1  
                # Increment count if already present
            else:
                window_items[item] = 1  
                # Initialize count if first time seen

        # Step 4: Compare window_items with required_items
        match = True  # Flag to check if the window meets requirements
        for item in required_items:  
        # Loop through required items
            # If item is missing or does not have the required quantity, 
            # set match to False
            if item not in window_items or window_items[item] != required_items[item]:
                match = False
                break  # No need to check further if there's a mismatch

        # Step 5: If the window matches the required items exactly, 
        # count it as a valid start day
        if match:
            valid_start_days += 1

    # Step 6: Return the total count of valid membership start days
    return valid_start_days

# Example Test Cases
print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], 
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", 
                "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))  # Expected Output: 3

print(solution(["apple"], [10], 
               ["banana", "banana", "banana", "banana", "banana", 
                "banana", "banana", "banana", "banana", "banana"]))  # Expected Output: 0
