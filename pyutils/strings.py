def reverse_string(s):
    return s[::-1]


def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")


def capitalize_words(s):
    return " ".join(word.capitalize() for word in s.split())
