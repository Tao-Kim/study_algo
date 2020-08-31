import sys

input = sys.stdin.readline
INFINITY = 987654321

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distanceList = [INFINITY] * (n + 1)


def solution(current, distance):
    nextDistance = distance + 1
    if distance + 1 <= k:
        for city in graph[current]:
            solution(city, nextDistance)
            distanceList[city] = min(distanceList[city], nextDistance)


solution(x, 0)


if distanceList.count(k) == 0:
    print(-1)
else:
    for index, distance in enumerate(distanceList):
        if distance == k:
            print(index)


"""
문제 : p339_특정 거리의 도시 찾기
시간 : 20분

접근 :
- 재귀를 이용하여 dfs로 풀었는데 bfs에 비해 상당히 비효율적인 것 같음


다른 사람 풀이 :
========================================================================================
bfs 풀이


from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)
========================================================================================


노트 : 
- 문제를 좀더 꼼꼼히 읽자.
"""

