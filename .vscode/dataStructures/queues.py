# FIFO
# First in first out

from collections import deque
queue = deque([])
# dodajemo
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)
# skidamo
queue.popleft()
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)
if not queue:
    print("empty")
