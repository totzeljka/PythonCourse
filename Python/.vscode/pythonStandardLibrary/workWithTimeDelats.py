from datetime import datetime, timedelta


td1 = datetime(2018, 11, 29) + timedelta(1)
td2 = datetime.now

duration = td2-td1

print(duration)
print("days", duration.days)
print("seconds", duration.seconds)

print("total seconds", duration.total_seconds())
