# Timedelta function demonstration
from datetime import datetime, timedelta
 
# Using current time
ini_time_for_now = datetime.now()

# Some another datetime
haloween = datetime(2022, 10, 31)
 
user = input('give a holiday')

usertwo = input('give the date of the previously selected holiday in YYYY, MM, DD form'

# printing calculated past_dates
int('Time until', user, ' - ', str(datetime(usertwo) - ini_time_for_now))