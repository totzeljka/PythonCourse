import time

# broj sekundi od pocetka mog operativnog sistema: 1688571211.9821458
# print(time.time())


def send_emails():
    for i in range(100000):
        pass

# stampace 0.0020580291748046875


start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)
