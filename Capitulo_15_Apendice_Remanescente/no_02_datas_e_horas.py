import datetime


my_date = datetime.date(2015, 10, 21)
print(my_date)

my_time = datetime.time(7, 28, 1)
print(my_time)

my_datetime = datetime.datetime(2015, 10, 21, 7, 28, 1)
print(my_datetime)

now = datetime.datetime.today()
print(now)

output = '{:%A, %B %d, %Y}'
print(output.format(my_date))
