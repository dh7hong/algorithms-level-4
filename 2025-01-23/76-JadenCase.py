def solution(s):
    # Split the string into words while keeping spaces (handling multiple spaces correctly)
    words = s.split(" ")

    # Convert each word to JadenCase
    jaden_words = [word.capitalize() for word in words]

    # Join the words back together with spaces
    return " ".join(jaden_words)

# Example test cases
print(solution("3people unFollowed me"))  # Expected output: "3people Unfollowed Me"
print(solution("for the last week"))      # Expected output: "For The Last Week"
print(solution("  hello   world  "))      # Expected output: "  Hello   World  "
print(solution("a bc dE Fg"))             # Expected output: "A Bc De Fg"
