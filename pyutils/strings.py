def reverse_string(s):
    return s[::-1]


def is_palindrome(s):
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def count_vowels(s):
    return sum(1 for c in s.lower() if c in "aeiou")


def capitalize_words(s):
    return " ".join(word.capitalize() for word in s.split())


def truncate(s, max_len, suffix="..."):
    if len(s) <= max_len:
        return s
    return s[:max_len - len(suffix)] + suffix


def snake_to_camel(s):
    parts = s.split("_")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


def camel_to_snake(s):
    import re
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", s)
    s = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", s)
    return s.lower()


def remove_duplicates_str(s):
    seen = set()
    result = []
    for c in s:
        if c not in seen:
            seen.add(c)
            result.append(c)
    return "".join(result)
