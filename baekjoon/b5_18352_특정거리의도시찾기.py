from collections import deque
INFINITY = 987654321
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distanceList = [INFINITY] * (n+1)
queue = deque()
queue.append((x, 0))

while queue:
    current, distance = queue.popleft()

    if distanceList[current] == INFINITY:
        distanceList[current] = distance

    if distance < k:
        for city in graph[current]:
            if distanceList[city] > distance + 1:
                queue.append((city, distance + 1))

if distanceList.count(k) == 0:
    print(-1)
else:
    for index, value in enumerate(distanceList):
        if value == k:
            print(index)


