from datetime import datetime, date

# Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(day, month, year,hour, minute,timestamp)

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
time_now = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_now)

# Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("Today is ", date_object)

# Calculate the time difference between now and new year.
new_year = date(year=2023, month=1, day=1)
now_year = date(year=now.year, month=now.month, day=now.day)
diff = new_year - now_year
print("The time left for new year is ", diff)

# Calculate the time difference between 1 January 1970 and now
now_year = date(year=now.year, month=now.month, day=now.day)
t1 = date(year=1970, month=1, day=1)
diff = now_year - t1
print("The time difference between now and 1st January 1970 is ", diff)

# Think, what can you use the datetime module for? Examples:
#    Time series analysis
#      - contains a fairly extensive set of tools for working with dates, times, and time-indexed data
#    To get a timestamp of any activities in an application
#      -To refer particular moments in time (eg 4th July, 2028 at 9:00 am)
#    Adding posts on a blog
#        -To identify the time when a post was uploaded or the time when something in the post
#         was downloaded by a user.

