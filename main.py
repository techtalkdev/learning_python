def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")  # Optional: make lowercase and remove spaces
    return cleaned == cleaned[::-1]


