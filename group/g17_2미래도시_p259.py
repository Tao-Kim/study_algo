import heapq
INFINITY = 987654321

n, m = map(int, input().split())
edgeList = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input())
    edgeList[a].append(b)
    edgeList[b].append(a)
    
x, k = map(int, input().split())


def dijkstra(start, end):
    countList = [INFINITY] * (n + 1)
    countList[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        count, current = heapq.heappop(heap)

        if count <= countList[current]:
            for edge in edgeList[current]:
                nextCount = count + 1
                if nextCount < countList[edge]:
                    countList[edge] = nextCount
                    heapq.heappush((nextCount, edge))

    return countList[end]


countK = dijkstra(1, k)
countX = dijkstra(k, x)

if countK == INFINITY or countX == INFINITY:
    print(-1)
else:
    print(countK+countX)