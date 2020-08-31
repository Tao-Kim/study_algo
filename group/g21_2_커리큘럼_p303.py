from collections import deque

n = int(input())

timeOfLectureList = [0]
edgeList = [[] for _ in range(n+1)]
previousLectureCountList = [0] * (n+1)

startTimeOfLectureList = [0 for _ in range(n+1)]

edgeQueue = deque()

for i in range(1, n+1):
    temp = list(map(int, input().split()))
    timeOfLectureList.append(temp[0])

    for j in temp[1:-1]:
        edgeList[j].append(i)
        previousLectureCountList[i] += 1

for i, count in enumerate(previousLectureCountList):
    if count == 0:
        edgeQueue.append(i)

while edgeQueue:
    current = edgeQueue.popleft()

    for i in edgeList[current]:
        startTimeOfLectureList[i] = max(startTimeOfLectureList[i], startTimeOfLectureList[current] + timeOfLectureList[current])
        previousLectureCountList[i] -= 1

        if previousLectureCountList[i] == 0:
            edgeQueue.append(i)

for i in range(1, n+1):
    print(startTimeOfLectureList[i] + timeOfLectureList[i])



