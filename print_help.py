#!/usr/bin/env python3
"""Help description of each available command.
Check current help prints to see the format.
Add new help_ function to the COMMS dict.
"""


def help_create():
    print("$ timetrack create NAME")
    print("  # Creates a profile which you can start a timer for.")

def help_set():
    print("$ timetrack set NAME")
    print("  # Sets the profile so that you can run start, stop, status on that profile.")

def help_start():
    print("$ timetrack start [NON_SET_PROFILE]")
    print("  # Starts the timer on the profile that is currently set.")
    print("OPTIONS:")
    print("  NON_SET_PROFILE: An existing profile name.")
    print("    Ex. $ timetrack start profile2")

def help_stop():
    print("$ timetrack stop [NON_SET_PROFILE]")
    print("  # Stops the timer on the profile that is currently set.")
    print("OPTIONS:")
    print("  NON_SET_PROFILE: An existing profile name.")
    print("    Ex. $ timetrack stop profile2")

def help_status():
    print("$ timetrack status [TIME_FORMAT] [START_DATE] [to] [END_DATE]")
    print("  # Shows the total time spent on profile that is currently set without options.")
    print("    # Ex. $ timetrack status")
    print("OPTIONS:")
    print("  TIME_FORMAT: h")
    print("    Ex. $ timetrack status h")
    print("  START_DATE to END_DATE")
    print("    Ex. $ timetrack status 2020-01-30 to 2020-02-20")

def help_delete():
    print("$ timetrack delete NAME")
    print("  # Deletes the specified profile.")

def help_add():
    print("$ timetrack add [DATE] TIME_AMT TIME_EXT")
    print("  # Adds time to today without [DATE].")
    print("    # Ex. $ timetrack add 5 hours")
    print("  # Adds time to without [DATE].")
    print("    # Ex. $ timetrack add 2020-01-30 5 hours")

def help_rename():
    print("$ ./timetrack.py rename NAME")
    print("  # Rename the current set profile to NAME.")

def help_csv():
    print("$ timetrack csv")
    print("  # Creates a csv file of the current set profile in the current directory.")

def help_list():
    print("$ timetrack list")
    print("  # Lists all available profiles.")

COMMS = {"create": help_create,
         "rename": help_rename,
         "set": help_set,
         "start": help_start,
         "stop": help_stop,
         "add": help_add,
         "list": help_list,
         "status": help_status,
         "delete": help_delete,
         "csv": help_csv}

def help_one(command):
    print()
    if COMMS.get(command, None):
        COMMS[command]()
    else:
        print(f"{command} was not found. Use -help to list all commands.")

def help_all():
    print()
    for item in COMMS:
        help_one(item)
