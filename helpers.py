#!/usr/bin/env python3
"""Module for functions. Contains all helper funcs of functions.py"""
from datetime import date
from datetime import timedelta
from datetime import datetime
TIME_MODE = None

def add_time(profile, seconds, d=None):
    """Adding time to a profile.
    Optional:
        d (str): Date option in string, else gets today's date.
    """
    _date = str(date.today())
    if d:
        _date = d

    if profile.times.get(_date, None):
        profile.times[_date] += seconds
    else:
        profile.times[_date] = seconds
    time_formatted = format_time(seconds)
    print(f"> ({_date}) {time_formatted} added to {profile.name}")
    return profile

def sub_time(profile, seconds, d=None):
    """Subtracting time to a profile.
    Optional:
        d (str): Date option in string, else gets today's date.
    """
    _date = str(date.today())
    if d:
        _date = d

    if profile.times.get(_date, None):
        profile.times[_date] -= seconds
    else:
        print(f"> Time has not been recorded for today, cannot subtract from 0.")
        profile.times[_date] = 0
        return profile
    if profile.times[_date] < 0:
        profile.times[_date] = 0
    time_formatted = format_time(seconds)
    print(f"> ({_date}) {time_formatted} subtracted from {profile.name}")
    return profile

def format_time_strings(times):
    """Converts time to string for format_time()"""
    res = []
    for t in times:
        if float(t[0]) == 0.0:
            continue
        elif float(t[0]) == 1:
            res += "1", t[1][:-1]
        else:
            # Rounding off as a string, not an int
            if len(t[0].split(".")) == 2:
                res += t[0].split(".")[0], t[1]
            else:
                res += t[0], t[1]
    if res:
        return " ".join(res)
    return 0

def format_time(seconds):
    """Args:
        mode (str): accepts 'h' or 'd' to stop the conversion and return
        the mode.
    """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    if TIME_MODE == "h":
        times = [(str(h), "hours"), (str(m), "mins")]
        return format_time_strings(times)
    d, h = divmod(h, 24)
    if TIME_MODE == "d":
        return (d, h, m, s)
    w, d = divmod(d, 7)
    times = [(str(w), "weeks"), (str(d), "days"), (str(h), "hours"),
             (str(m), "mins"), (str(s), "secs")]
    return format_time_strings(times)

def date_range(start, end):
    """Returns:
        r (list): List of dates in the range of `start` and `end`
    """
    st = datetime.strptime(start, "%Y-%m-%d").date()
    en = datetime.strptime(end, "%Y-%m-%d").date()
    r = [str(st + timedelta(days=x)) for x in range(0, (en - st).days)]
    return r

def get_sec(time_args):
    """Converts readable time into seconds. Takes in only mins and hours.
    Args:
        time_args (str): Readable time format like '5 hours'.
    Returns: _ (int): Seconds of the readable time.
    """
    time_ext = time_args[1::2]
    times = time_args[::2]
    h, m = (0, 0)
    if len(times) == 2:
        h = times[0]
        m = times[1]
    elif len(time_ext) == 1 and time_ext[0] in ["hour", "hours", "hr", "hrs"]:
        h = times[0]
    elif len(time_ext) == 1 and time_ext[0] in ["min", "mins", "minute", "minutes"]:
        m = times[0]
    return int(h) * 3600 + int(m) * 60

def validate_date(string):
    try:
        datetime.strptime(string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def get_day_name(d):
    """Returns the day's name."""
    obj = datetime.strptime(d, '%Y-%m-%d')
    name = obj.ctime().split()[0]
    return name
