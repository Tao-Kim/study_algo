from collections import deque

n = int(input())

lectures_time = [0] * (n+1)
lectures_graph = [[] for _ in range(n+1)]
lectures_count = [0] * (n+1)


for i in range(1, n+1):
    input_list = list(map(int, input().split()))

    lectures_time[i] = input_list[0]

    for pre in input_list[1:-1]:
        lectures_count[i] += 1
        lectures_graph[pre].append(i)



queue = deque()

for i in range(1, n+1):
    if lectures_count[i] == 0:
        queue.append(i)

while queue:
    current = queue.popleft()

    for i in lectures_graph[current]:
        lectures_count[i] -= 1
        lectures_time[i] += lectures_time[current]
        if lectures_count[i] == 0:
            queue.append(i)


for lecture_time in lectures_time[1:]:
    print(lecture_time)