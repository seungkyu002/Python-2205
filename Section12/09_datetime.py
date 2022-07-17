import datetime as dt

print(dt.datetime.now())
birthday = dt.date(2022,6,22)
print(birthday)

date = dt.datetime.now()
print(date.year)
print(date.month)
print(date.day)
print(date.hour)
print(date.minute)
print(date.second)
print(date.microsecond)
# date.day = 30 # 수정 X

date = date.replace(2022,12,31,0,0,0)
print(date)

today = dt.datetime.now()
tomorrow = today + dt.timedelta(days=1)
print(dt.timedelta(days=1))
print(tomorrow)

next_week = today + dt.timedelta(weeks=1)
print(next_week)

date1 = dt.date(2022,6,16)
date2 = dt.date(2022,6,17)
print(date2 - date1)
print((date2 - date1).total_seconds() // (24 * 60 * 60))

# 오늘 날짜 기준으로 수능날까지 D-Day를 출력
date1 = dt.date(2022,6,15)
date2 = dt.date(2022,11,17)
print((date2 - date1).total_seconds() // (24 * 60 * 60))