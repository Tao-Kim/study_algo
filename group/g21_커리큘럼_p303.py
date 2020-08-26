from collections import deque

n = int(input())

previousLectureCount = [0] * (n + 1)
lectureGraph = [[] for i in range(n + 1)]
lectureTime = [0] * (n + 1)
lectureStartTime = [0] * (n + 1)
currentTime = 0

for i in range(1, n+1):
    temp = list(map(int, input().split()))
    lectureTime[i] = temp[0]
    
    for j in range(1, len(temp)):
        if temp[j] != -1:
            previousLectureCount[i] += 1
            lectureGraph[temp[j]].append(i)
        

taskDeque = deque()
for i in range(1, n+1):
    if previousLectureCount[i] == 0:
        taskDeque.append(i)

while taskDeque:
    current = taskDeque.popleft()
    currentTime = lectureStartTime[current]

    for lecture in lectureGraph[current]:
        lectureStartTime[lecture] = max(lectureStartTime[lecture], currentTime + lectureTime[current])

        previousLectureCount[lecture] -= 1
        if previousLectureCount[lecture] == 0:
            taskDeque.append(lecture)
        
for i in range(1, n+1):
    print(lectureTime[i] + lectureStartTime[i])



"""
문제 : p303_커리큘럼
시간 : 38분

접근 :
해설과 개념은 같음.
수강까지 걸리는 최소 시간을 구하는 부분에서 머릿속에서 전개한 알고리즘에 따라
startTime으로 작성했는데 startTime보다 endTime이 더 효율적인 것 같음



다른 사람 풀이 :
========================================================================================
해설 :
========================================================================================

노트 :
- 풀기는 했는데 그래프 문제풀이가 아직 익숙하지 않아서 시간이 오래걸림
- 그래프 관련 문제 많이 풀어볼 것
"""