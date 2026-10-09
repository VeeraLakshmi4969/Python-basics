import datetime

date = datetime.date(2025,1,2)
print(date)
today = datetime.date.today()
print(today)
time = datetime.time(22,8,9)
print(time)
now = datetime.datetime.now()
print(now)

string_formate_time = now.strftime("%D %m %y %h:%M:%S")
print(string_formate_time)
target_date = datetime.datetime(2030,2,3)
if target_date<now:
    print("This year was past")
    print(target_date)
else:
    print("This year is future year")
    print(target_date)
    