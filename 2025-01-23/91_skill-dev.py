def solution(progresses, speeds):
    # Step 1: Compute the number of days each feature needs to reach 100%
    days_required = []  
    # List to store days needed for each feature

    for i in range(len(progresses)):
        remaining_work = 100 - progresses[i]  
        # Work left to complete
        days = (remaining_work + speeds[i] - 1) // speeds[i]  
        # Ceiling division
        days_required.append(days)  
        # Store the computed days

    # Step 2: Process the deployment in order
    deploy_batches = []  
    # Stores the number of features deployed together
    first_deploy_day = days_required[0]  
    # The first feature's deployment day
    count = 0  
    # Count features in a batch

    for days in days_required:
        if days > first_deploy_day:
            # A new batch starts when a feature 
            # takes longer than the current batch
            deploy_batches.append(count)
            count = 1  
            # Start new batch count
            first_deploy_day = days  
            # Update the first deployable day
        else:
            count += 1  # Add to the current batch

    # Add the last batch count
    deploy_batches.append(count)

    return deploy_batches

# Example Test Cases
print(solution([93, 30, 55], [1, 30, 5])) 
# Output: [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  
# Output: [1, 3, 2]
