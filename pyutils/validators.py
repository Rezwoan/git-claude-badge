import re


def is_url(s):
    pattern = re.compile(
        r"^(https?|ftp)://"
        r"(\w+(-\w+)*\.)+[a-z]{2,}"
        r"(/[^\s]*)?$",
        re.IGNORECASE,
    )
    return bool(pattern.match(s))


def is_ip(s):
    parts = s.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
    return True
