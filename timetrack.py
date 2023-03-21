#!/usr/bin/env python3
"""Entry point for timetrack. Handles arguments.
Add newly created commands from functions.py to COMM.
If new command takes only a profile name, add to COMM_SINGLE.
If new command can take optional arguments, add to COMM_MULTI.
"""
import sys
import print_help as h
import functions as func
import database as db
COMM_MULTI = {"start": func.start_timer,
              "stop": func.stop_timer,
              "status": func.status_profile,
              "add": func.timeadd_profile,
              "sub": func.timesub_profile,
              "list": func.list_profile,
              "csv": func.csv_profile}
COMM_SINGLE = {"create": func.create_profile,
               "set": func.set_profile,
               "delete": db.delete,
               "rename": func.rename_profile}


def argparser(args):
    profile = func.A_PROFILE
    if "help" in args[0]:
        if len(args) == 2:
            h.help_one(args[1])
        else:
            h.help_all()
    if COMM_MULTI.get(args[0], None):
        if len(args) > 1:
            options = args[1:]
            COMM_MULTI[args[0]](profile, options)
        else:
            COMM_MULTI[args[0]](profile)
    elif COMM_SINGLE.get(args[0], None):
        if len(args) == 2:
            COMM_SINGLE[args[0]](args[1])
        else:
            print(f"{args[0]} requires a profile name.")
    else:
        print(f"{args[0]} is not a command. Use -help for a list of commands.")

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) > 0:
        argparser(args)
    else:
        print("Please enter an argument or use -help to see more details.")
