<h1 align="center">Project 3racker</h1>
<p align="center">
  <img src="https://images.unsplash.com/photo-1512856246663-647a81ef198e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2005&q=80" height=400px>
</p>

A simple terminal tool that tracks times for projects/activities.

---

## Linux Setup :wrench:
  - Run `./setup`

---

## Commands


*Anything variable between []s are optional*
*All date variables are in YEAR-MONTH-DAY format*

- `set NAME`: Sets the profile NAME to be tracked.
- `create NAME`: Creates the profile NAME.
- `delete NAME`: Deletes the profile NAME.
- `rename NEWNAME`: Renames the set profile to NEWNAME.
- `start`: Starts the timer on the current set profile.
  - `start [NAME]`
- `stop`: Stops the timer on the current set profile.
  - `stop [NAME]`
- `list`: Lists all profiles available.
- `status`: Checks the total amount of time spent in current set profile.
  - `status [TIME_FORMAT] [DATE_RANGE: START to END]`
    - `TIME_FORMAT`: `h` sets the return to hours only.
    - `DATE_RANGE`: Ex: 2020-01-20 to 2020-02-20
- `csv`: Creates a csv file in the current directory of the current set profile.
- `add TIME`: Adds time to the current set profile. TIME ex: 5 mins
  - `add TIME [DATE]`
- `sub TIME`: Subs time from the current set profile. TIME ex: 5 mins
  - `sub TIME [DATE]`

---

## Examples

```
$ timetrack create demo
$ timetrack create demo-not-set
$ timetrack list
$ timetrack set demo
$ timetrack start
$ timetrack start demo-not-set
$ timetrack stop
$ timetrack stop demo-not-set
$ timetrack delete demo-not-set
$ timetrack add 5 mins
$ timetrack sub 1 min
$ timetrack status
$ timetrack status h
$ timetrack status 2020-01-20
$ timetrack status 2020-01-20 to 2020-02-20
$ timetrack status h 2020-01-20 to 2020-02-20
$ timetrack csv
$ timetrack rename newdemo
```

---

## Author
* **Lebi OLuwasoji** - 
* **Oluwatobi Amoniyan** - amoniyano1@gmail.com
