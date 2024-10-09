import datetime

start = datetime.date(2023, 11, 1)
periods = 30
daterange = []
for day in range(periods):
    print(f'{day:02}')
    # date = (start + datetime.timedelta(days=day)).isoformat()
    # daterange.append(date)
print(daterange)