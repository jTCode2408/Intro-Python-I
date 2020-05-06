"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
  ##2 args

and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
   ##if NO INPUT SPECIFIED, print CURRENT month(DATETIME)

 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
   ##if MONTH ONLY, print MONTH PASSED IN for CURRENT year(datetime)

 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
   ##if BOTH month and year, render calendar for THAT MONTH/YEAR inputted

 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
##NO INPUT GIVEN, print message prompting for args

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime





#check for input values in term
inputs = sys.argv
now = datetime.now()

month = now.month
year = now.year
#if input not specified, return current month only
if len(inputs) == 1:
  print(month) ##should return this month
  pass
#if 1 arg given, assume to be month. return that month AND ADD CURRENT year
elif len(inputs) == 2:
  month=int(inputs[1]) #index 1, should be month position

#if BOTH, redner both
elif len(inputs) == 3:
  month = int(inputs[1])
  year=int(inputs[2]) #index 2, shold be year positon
#if NO ARGS, prompt
else:
  print("format expected: 14_cal.py [month] [year]")

#print cal in term

cal = calendar.TextCalendar()
cal.prmonth(year, month)