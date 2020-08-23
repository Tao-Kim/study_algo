x = int(input())

countList = [x+1] * (x + 1)
countList[x] = 0

for i in range(x,0,-1):
    if i % 5 == 0:
        if countList[i // 5] > countList[i] + 1:
            countList[i // 5] = countList[i] + 1
    if i % 3 == 0:
        if countList[i // 3] > countList[i] + 1:
            countList[i // 3] = countList[i] + 1
    if i % 2 == 0:
        if countList[i // 2] > countList[i] + 1:
            countList[i // 2] = countList[i] + 1
    if countList[i - 1] > countList[i] + 1:
        countList[i - 1] = countList[i] + 1
    
print(countList[1])

"""
문제 : p217_1로 만들기
시간 : 14분

접근 :
다이나믹 프로그래밍으로 각 숫자 별로 최소 연산수를 기억시키며 처리함


다른 사람 풀이 :
========================================================================================
해설 : 0에서 부터 출발하는 방식
  
# 정수 X를 입력 받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1000001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
========================================================================================

노트 :
- 
"""