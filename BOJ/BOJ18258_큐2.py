import sys
from collections import deque
input = sys.stdin.readline

N=int(input())
queue=deque([])
for _ in range(N):
    string = input().strip()
    chunk = string.split()
    if chunk[0] == "push":
        queue.append(chunk[1])
    elif chunk[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif chunk[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif chunk[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif chunk[0] == "size":
        print(len(queue))
    elif chunk[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)