import datetime

def format_timestamp(ts):
    return datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")

def percent_change(old, new):
    try:
        return round(((new - old) / old) * 100, 2)
    except ZeroDivisionError:
        return float('inf')
