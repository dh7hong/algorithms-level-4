def solution(survey, choices):
    # Define personality type pairs for each indicator
    personality_pairs = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    
    # Initialize a dictionary to store scores for each personality type
    scores = {}
    for pair in personality_pairs:
      for char in pair:
        scores[char] = 0
    
    # Define score values corresponding to choices
    score_values = {1: -3, 2: -2, 3: -1, 4: 0, 5: 1, 6: 2, 7: 3}
    
    # Process each question in the survey
    for i in range(len(survey)):
        first_type, second_type = survey[i]
        score = score_values[choices[i]]  # Get the score value
        
        if score < 0:
            scores[first_type] += abs(score)  # Add score to first type if negative
        else:
            scores[second_type] += score  # Add score to second type if positive
    
    # Determine the final personality type
    result = ""
    for first_type, second_type in personality_pairs:
        if scores[first_type] > scores[second_type]:
            result += first_type
        elif scores[first_type] < scores[second_type]:
            result += second_type
        else:
            result += min(first_type, second_type)  # Choose the lexicographically smaller one
    
    return result

# Example test cases
print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))  # Output: "TCMA"
print(solution(["TR", "RT", "TR"], [7, 1, 3]))  # Output: "RCJA"