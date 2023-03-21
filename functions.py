#!/usr/bin/env python3
"""Module for timetrack.py. Command functions for timetrack.py
Any new functions should have a help description function in print_help.py
"""
import helpers as h
import database as db
import time
A_NAME = db.read_active()["active"]
A_PROFILE = db.read(db.Profile, A_NAME)

def create_profile(name):
    new = db.Profile(name, False, 0, {})
    db.update(new)
    print(f"> Created profile: {name}")

def rename_profile(profile, name):
    prev = profile.name
    profile.name = name
    db.update(profile)
    print(f"> Renamed profile {prev} to {name}.")

def set_profile(name):
    active = db.read_active()
    if list(active)[0] == name:
        print(f"> Profile {name} is already active.")
    else:
        profiles = db.read_all()
        if name in profiles:
            db.update_active({"active": name})
            print(f"> Profile {name} is now active.")
        else:
            print(f"> Profile {name} was not found. Please use create to make this profile.")

def start_timer(profile, name=None):
    if name:
        profile = db.read(db.Profile, name[0])
    if profile.start == False:
        profile.begin = time.time()
        profile.start = True
        db.update(profile)
        print(f"> Started timer for {profile.name}")
    else:
        print(f"> Timer for {profile.name} is already started.")

def stop_timer(profile, name=None):
    if name:
        profile = db.read(db.Profile, name[0])
    if profile.start == True:
        total = time.time() - profile.begin
        profile = h.add_time(profile, total)
        profile.start = False
        db.update(profile)
        print(f"> Stopped timer for {profile.name}")
    else:
        print(f"> Profile {profile.name} has not been started.")

def status_profile(profile, dates=None):
    """Default mode returns total time.
    Modes:
        range: Returns total time for date range.
    """
    all_times = profile.times
    if dates and dates[0] == "h":
        h.TIME_MODE = "h"
        dates = dates[1:]
    if dates:
        if len(dates) == 1:
            d = dates[0]
            total = all_times.get(d, 0)
            print(f"> ({profile.name}) {d}: {h.format_time(total)}")
        elif len(dates) == 3:
            date_range = h.date_range(dates[0], dates[2])
            total = 0
            for d in date_range:
                total += all_times.get(d, 0)
            print(f"> ({profile.name}) {' '.join(dates)}: {h.format_time(total)}")
        else:
            pass
    else:
        total = sum(list(all_times.values()))
        print(f"> Set profile is {profile.name}.")
        print(f"> Total time: {h.format_time(total)}")

def timeadd_profile(profile, time_args):
    """Checks if first argument is a date. If date, inserts time into date.
    Else, it inserts into today.
    """
    _date = None
    if "-" in time_args[0]:
        if h.validate_date(time_args[0]):
            _date = time_args[0]
        time_args = time_args[1:]
    secs = h.get_sec(time_args)
    if _date:
        profile = h.add_time(profile, secs, _date)
    else:
        profile = h.add_time(profile, secs)
    db.update(profile)

def timesub_profile(profile, time_args):
    _date = None
    if "-" in time_args[0]:
        if h.validate_date(time_args[0]):
            _date = time_args[0]
        time_args = time_args[1:]
    secs = h.get_sec(time_args)
    if _date:
        profile = h.sub_time(profile, secs, _date)
    else:
        profile = h.sub_time(profile, secs)
    db.update(profile)

def list_profile(placeholder):
    """Args:
        placeholder: Ignore.
    """
    profiles = list(db.read_all())
    print(f"> Profiles: {' '.join(profiles)}")

def csv_profile(profile):
    """TODO Manipulate into lists to join with ','"""
    times = profile.times
    layout = [(profile.name,)]
    for t in times:
        d_name = h.get_day_name(t)
        layout.append((t, d_name, h.format_time(times[t])))
    path = db.create_csv_path(profile.name)
    with open(path, "w+") as f:
        for r in layout:
            f.write(",".join(r))
            f.write("\n")
        print(f"> Created {path}")
