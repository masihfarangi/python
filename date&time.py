from datetime import date
from datetime import datetime

today = date.today()
print("today is : {}".format(today))

print("day:" , today.day)
print("month:" , today.month)
print("year:" , today.year)
print("week day: " , today.weekday())

today = datetime.now()
print("the current date and time is :" , today)