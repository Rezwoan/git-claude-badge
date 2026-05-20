from datetime import date


def days_between(d1, d2):
    return abs((d2 - d1).days)


def is_weekend(d):
    return d.weekday() >= 5
