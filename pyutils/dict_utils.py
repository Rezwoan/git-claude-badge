def invert(d):
    return {v: k for k, v in d.items()}


def deep_merge(base, override):
    result = dict(base)
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def flatten_keys(d, sep=".", prefix=""):
    items = {}
    for k, v in d.items():
        full_key = f"{prefix}{sep}{k}" if prefix else k
        if isinstance(v, dict):
            items.update(flatten_keys(v, sep=sep, prefix=full_key))
        else:
            items[full_key] = v
    return items
