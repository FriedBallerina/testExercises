def is_palindrome(word):
    
    if word.lower() == word.lower()[::-1]:
        return True
    else:
        return False

print(is_palindrome('Deleveled'))