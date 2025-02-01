# def solution(today, terms, privacies):
#     # Convert 'YYYY.MM.DD' string to integer format (YYYY, MM, DD)
#     def parse_date(date):
#         y, m, d = map(int, date.split('.'))
#         return y, m, d

#     # Convert terms list into a dictionary for quick lookup
#     term_dict = {}
#     for term in terms:
#         key, months = term.split()
#         term_dict[key] = int(months)

#     # Parse today's date
#     today_y, today_m, today_d = parse_date(today)

#     result = []  # Store indices of expired data entries

#     # Process each privacy entry
#     for i, entry in enumerate(privacies):
#         date_str, term_key = entry.split()  # Extract date and term type
#         start_y, start_m, start_d = parse_date(date_str)

#         # Calculate expiry date
#         expiry_m = start_m + term_dict[term_key]  # Add storage duration
#         expiry_y = start_y + (expiry_m - 1) // 12  # Adjust year
#         expiry_m = (expiry_m - 1) % 12 + 1  # Adjust month (1-12 range)
        
#         expiry_d = start_d - 1  # Subtract 1 day for expiration rule
#         if expiry_d == 0:  # If day becomes 0, adjust the month
#             expiry_m -= 1
#             if expiry_m == 0:  # If month becomes 0, adjust the year
#                 expiry_m = 12
#                 expiry_y -= 1
#             expiry_d = 28  # Every month is 28 days

#         # Check if expired
#         if (expiry_y, expiry_m, expiry_d) < (today_y, today_m, today_d):
#             result.append(i + 1)  # Store index (1-based)

#     return result



# def day_calculator(string):
#     print(f'{string[:4]}*365 + {string[4:6]}*28 + {string[6:8]}')
#     return int(string[:4])*365 + int(string[4:6])*28 + int(string[6:8])


# def solution(today, terms, privacies):

#     # removing the dots from the list 'privacies' and the string 'today'
#     today = "".join(today.split("."))
#     for i in range(len(privacies)):
#         privacies[i] = "".join(privacies[i].split("."))

#     # changing the list 'terms' into a dictionary
#     terms_dict = {}
#     for i in range(len(terms)):
#         terms_dict[terms[i][0]] = int(terms[i][2:])

#     lst = []
#     for i in range(len(privacies)):
#         if day_calculator(privacies[:8]) + terms_dict[privacies[i][-1]]*28 > day_calculator(today):
#             lst.append(i+1)

#     return lst

# # Example test cases
# print(solution("2022.05.19", ["A 6", "B 12", "C 3"], 
#                ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))  
# # Output should be: [1, 3]

# print(solution("2020.01.01", ["Z 3", "D 5"], 
#                ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))  
# # Output should be: [1, 4, 5]

def day_calculator(date_str):
    """Converts a date (YYYYMMDD format) into a numerical value for comparison."""
    print(f'{int(date_str[:4])} * 12 * 28 + {int(date_str[4:6])} * 28 + {int(date_str[6:8])}')
    year, month, day = int(date_str[:4]), int(date_str[4:6]), int(date_str[6:8])
    return year * 12 * 28 + month * 28 + day  # Convert year and month to days

def solution(today, terms, privacies):
    # Convert 'today' into numeric day format
    today = "".join(today.split("."))
    today_days = day_calculator(today)

    # Convert 'terms' list into a dictionary for quick lookup
    terms_dict = {}
    for term in terms:
        key, value = term.split()
        terms_dict[key] = int(value) * 28  # Convert months to days

    expired_list = []
    
    for i in range(len(privacies)):
        # Extract date and term type from privacy entry
        privacy_data = privacies[i].split()
        privacy_date = "".join(privacy_data[0].split("."))  # Remove dots
        term_type = privacy_data[1]  # Extract term type

        # Calculate expiration date
        expiry_days = day_calculator(privacy_date) + terms_dict[term_type] - 1

        # If expired, add to result list
        if expiry_days < today_days:
            expired_list.append(i + 1)  # 1-based index

    return expired_list

# Example test cases
print(solution("2022.05.19", ["A 6", "B 12", "C 3"], 
               ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))  
# Output: [1, 3]

print(solution("2020.01.01", ["Z 3", "D 5"], 
               ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))  
# Output: [1, 4, 5]
