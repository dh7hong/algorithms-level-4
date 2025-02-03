def solution(id_list, report, k):
    # Step 1: Initialize data structures
    report_set = set(report)  # Remove duplicate reports
    
    # Create a dictionary to track which users each user has reported
    user_reports = {}
    for user in id_list:
        user_reports[user] = set()
    
    # Create a dictionary to count the number of times each user has been reported
    report_count = {}
    for user in id_list:
        report_count[user] = 0
    
    # Step 2: Process reports
    for r in report_set:
        reporter, reported = r.split()
        user_reports[reporter].add(reported)
        report_count[reported] += 1
    
    # Step 3: Determine suspended users
    suspended_users = set(filter(lambda user: report_count[user] >= k, id_list))
    
    # Step 4: Count emails for each user
    result = []
    for user in id_list:
        email_count = len(user_reports[user] & suspended_users)
        result.append(email_count)
    
    return result

# Test cases
id_list1 = ["muzi", "frodo", "apeach", "neo"]
report1 = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k1 = 2
print(solution(id_list1, report1, k1))  # Expected Output: [2,1,1,0]

id_list2 = ["con", "ryan"]
report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k2 = 3
print(solution(id_list2, report2, k2))  # Expected Output: [0,0]