def count_lines(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def find_by_extension(directory, ext):
    import os
    if not ext.startswith("."):
        ext = "." + ext
    matches = []
    for root, _, files in os.walk(directory):
        for name in files:
            if name.endswith(ext):
                matches.append(os.path.join(root, name))
    return matches


def read_json(filepath):
    import json
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(filepath, data, indent=2):
    import json
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent)
