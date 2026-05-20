import re


def is_url(s):
    pattern = re.compile(
        r"^(https?|ftp)://"
        r"(\w+(-\w+)*\.)+[a-z]{2,}"
        r"(/[^\s]*)?$",
        re.IGNORECASE,
    )
    return bool(pattern.match(s))
