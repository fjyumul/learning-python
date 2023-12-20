#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


# TODO: import the calendar module
import calendar
from datetime import datetime

# TODO: create a plain text calendar
# year = datetime.now().year
# month = datetime.now().month

# c = calendar.monthcalendar(year, month)
# # print(c)
# print(len([i for i in calendar.monthcalendar(year, month)]))

# TODO: create an HTML formatted calendar
# today = datetime.today()
# days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
# print(today.weekday())
# print("Tomorrow will be "+days[(today.weekday()+1)])

# TODO: loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month

  
# TODO: The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms


# TODO: Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

import calendar
import datetime
year = datetime.datetime.now().year
cal = calendar.TextCalendar(calendar.SUNDAY)
print(cal.formatmonth(year,1,0,0))
# for m in range(1,13):
#     print(cal.formatmonth(year, m, 0, 0))