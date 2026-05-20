def rotate(lst, n):
    if not lst:
        return lst
    n = n % len(lst)
    return lst[n:] + lst[:n]


def dedupe_ordered(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def partition(lst, predicate):
    trues = [x for x in lst if predicate(x)]
    falses = [x for x in lst if not predicate(x)]
    return trues, falses
