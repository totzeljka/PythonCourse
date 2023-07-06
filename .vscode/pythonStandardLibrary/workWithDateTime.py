from datetime import datetime
import time


dtf = datetime(2018, 11, 29)
now = datetime.now()
# https://docs.python.org/3/library/time.html
dtl = datetime.strptime("2015/03/09", "%Y/%m/%d")

# za pretvatanje timestempa u datumvreme objekt
dt_tmst = datetime.fromtimestamp(time.time())
# pretvara datetime objekat u string obrnuto od strptime


print(f"{dtf.year}/{dtf.month}")
print(dtf)
print(now)
print(dtl)
print(dt_tmst)

print(dt_tmst > dtf)

print(dt_tmst < dtf)
