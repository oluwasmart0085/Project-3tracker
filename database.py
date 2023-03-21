#!/usr/bin/env python3
"""JSON Database.
Anything that reads or writes to DATABASE should mainly take the class models
in here as an argument.
"""
import ujson as json
import os
ABSPATH = os.path.dirname(os.path.realpath(__file__))
DATABASE = os.path.join(ABSPATH, ".time.json")
ACTIVE = os.path.join(ABSPATH, ".active.json")


class Profile:
    """Main container class"""
    __slots__ = ("name", "start", "begin", "times",)
    def __init__(self, name, start, begin, times):
        self.name = name
        self.start = start
        self.begin = begin
        self.times = times

def read_active():
    if os.path.exists(ACTIVE):
        with open(ACTIVE, "r") as f:
            data = json.load(f)
    else:
        with open(ACTIVE, "w") as f:
            data = {"active": ""}
            json.dump(data, f)
    return data

def update_active(data):
    with open(ACTIVE, "w+") as f:
        json.dump(data, f)

def read_all():
    if os.path.exists(DATABASE):
        with open(DATABASE, "r") as f:
            data = json.load(f)
    else:
        with open(DATABASE, "w") as f:
            f.write("{}")
            data = {}
    return data

def read(obj, name):
    """Args:
        obj (obj): Empty container class specifying which key to grab.
    Returns:
        _ (obj): `obj` container with data of `name`
    """
    data = read_all()
    if data.get(name, None):
        if obj == Profile:
            start = data[name]["start"]
            begin = data[name]["begin"]
            times = data[name]["times"]
            return Profile(name, start, begin, times)
    else:
        print(f"> Could not find profile {name}")
        quit()

def update_all(data):
    with open(DATABASE, "w+") as f:
        json.dump(data, f)

def update(profile):
    """Args:
        profile (obj): Class of Profile
    """
    data = read_all()
    if isinstance(profile, Profile):
        new_data = {"start": profile.start, "times": profile.times, "begin": profile.begin}
        data[profile.name] = new_data
        update_all(data)

def delete(name):
    """Deletes only first key tier (profiles only) in dict."""
    data = read_all()
    if data.get(name, None):
        del data[name]
        update_all(data)
        print(f"> Profile {name} has been deleted")
    else:
        print(f"> Profile {name} was not found")

def create_csv_path(name):
    return os.path.join(os.getcwd(), (name + ".csv"))
