def solution(priorities, location):
    # Step 1: Create a list of tuples (index, priority) 
    # to track the original positions
    queue = []
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))  
        # Append index and priority as a tuple

    execution_order = 0  
    # Track the execution order

    while queue:
        current = queue.pop(0)  
        # Take the first process in the queue

        # Check if any process in the queue has a higher priority
        higher_priority_exists = False
        for item in queue:
            if current[1] < item[1]:
                higher_priority_exists = True
                break  
              # No need to check further

        if higher_priority_exists:
            queue.append(current)  
            # Put it back at the end of the queue
        else:
            execution_order += 1  
            # Execute the process

            # If it's the target process, return its execution order
            if current[0] == location:
                return execution_order

# Example Test Cases
print(solution([2, 1, 3, 2], 2))  # Output: 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # Output: 5
