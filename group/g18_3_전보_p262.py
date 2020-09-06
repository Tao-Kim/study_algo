import heapq

INFINITY = 987654321
n, m, c = map(int, input().split())

edges = [[] for _ in range(n+1)]

for _ in range(m):
    x, y, z = map(int, input().split())
    edges[x].append((z, y))


distance = [INFINITY] * (n+1)
distance[c] = 0

heap = []
heapq.heappush(heap, (0, c))


while heap:
    current_distance, current = heapq.heappop(heap)
    
    if distance[current] < current_distance:
        continue
    
    else:
        for (city_distance, city) in edges[current]:
            next_distance = city_distance + current_distance
            if next_distance < distance[city]:
                distance[city] = next_distance
                heapq.heappush(heap, (next_distance, city))


count = 0
max_distance = 0

for dist in distance:
    if dist != INFINITY:
        count += 1
        max_distance = max(dist, max_distance)

print(count - 1, max_distance)
