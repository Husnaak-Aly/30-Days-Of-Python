from datetime import datetime, date

#1. Get the current day, month, year, hour, minute and timestamp from datetime module
# now = datetime.now()
# print(now)


#2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
# now = datetime.now()
# format_date = now.strftime("%m/%d/%Y, %H:%M:%S")
# print(format_date)


#3. Today is 5 December, 2019. Change this time string to time
# date_string = '5 December, 2019'
# date_object = datetime.strptime(date_string, "%d %B, %Y")
# print(date_object)


#4. Calculate the time difference between now and new year.
# current_date = date(year = 2026, month = 10, day = 13)
# new_year = date(year = 2027, month = 1, day = 1)
# time_left = new_year - current_date
# print('Time left for new year:', time_left)


#4. Calculate the time difference between 1 January 1970 and now.
# year_1970 = datetime(year = 1970, month = 1, day = 1 )
# current_date = datetime.now()
# time_diff = current_date - year_1970
# print(time_diff)


