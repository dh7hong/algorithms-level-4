def solution(keymap, targets):
    # Dictionary to store the minimum presses required for each character
    press_count = {}

    # Step 1: Build the dictionary
    for i, key in enumerate(keymap):  # Iterate through each key in the keymap
        for j, char in enumerate(key):  # Iterate through characters in the key
            if char in press_count:
                press_count[char] = min(press_count[char], j + 1)  # Store the minimum key press
            else:
                press_count[char] = j + 1  # Store the first occurrence key press

    # Step 2: Process each target string
    result = []  # Store results for each target
    for target in targets:
        total_presses = 0  # Count of key presses for the target string
        for char in target:
            if char in press_count:
                total_presses += press_count[char]  # Add key press count for this character
            else:
                total_presses = -1  # If character is missing in keymap, set to -1
                break  # No need to check further, as the word cannot be formed
        result.append(total_presses)  # Append result for this target string

    return result
