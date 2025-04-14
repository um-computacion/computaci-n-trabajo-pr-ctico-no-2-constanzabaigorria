def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
