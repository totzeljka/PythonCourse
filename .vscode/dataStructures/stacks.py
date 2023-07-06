# LIFO

# last in first out

browsing_session = []
# da se doda na stak
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
# da se skine s vrha staka
last = browsing_session.pop()

print(last)
print(browsing_session)
print("redirecting ", browsing_session[-1])
if not browsing_session:
    print("disable")
