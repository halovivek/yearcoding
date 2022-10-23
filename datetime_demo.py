import datetime
today = datetime.datetime.today().date()
current_time = datetime.datetime.today().time()
current_date = datetime.datetime.today()
print(current_date)
print(today)
print(current_time)
time_format = current_date.strftime('%d-%m-%y %H-%M-%S')
print(time_format)
