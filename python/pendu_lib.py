# Pendulum library deals with date/timezone

# import library
import pendulum
dt = pendulum.datetime(2020, 11, 27)
print(dt)

#local() creates datetime instance with local timezone
local = pendulum.local(2020, 11,27)
print(local)
print(local.timezone.name)



# Converting Timezones


# Getting current UTC time
utc_time = pendulum.now('UTC')

# Switching current timezone to
# Kolkata timezone using in_timezone().
kolkata_time = utc_time.in_timezone('Asia/Kolkata')
print('Current Date Time in Kolkata =', kolkata_time)

# Generating Sydney timezone
sydney_tz = pendulum.timezone('Australia/Sydney')

# Switching current timezone to
# Sydney timezone using convert().
sydney_time = sydney_tz.convert(utc_time)
print('Current Date Time in Sydney =', sydney_time)



# Date Time Manipulations

# creating datetime instance
date = pendulum.datetime(2020, 11, 27)
print(date)

# Manipulating datetime object using add()
date = date.add(years=5)
print(date)

# Manipulating datetime object using subtract()
date = date.subtract(months = 1)
print(date)

# Similarly you can add or subtract
# months,weeks,days,hours,minutes
# individually or all at a time.
date = date.add(years=3, months=2, days=6,
			hours=12, minutes=30, seconds=45)

print(date)

