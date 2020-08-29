n, m = map(int, input().split())

ballList = tuple(map(int, input().split()))

allSize = len(ballList)
allCase = allSize * (allSize-1) // 2

for i in range(1, m+1):
    size = ballList.count(i)
    case = size * (size-1) //2
    allCase -= case

print(allCase)



"""
문제 : p315_볼링공고르기
시간 : 6분

접근 :
두개를 고를 수 있는 모든 경우의 수에 같은 무게를 고르는 경우의 수들을 빼서 구함

다른 사람 풀이 :
========================================================================================
공번호가 아니라 무게로 경우의 수를 푼 문제로
a가 특정 무게를 선택할 경우 b는 나머지 무게의 경우의 수만큼 고를 수 있다는 점을 이용
- 순서가 상관없는 경우의 수이기에 가능

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱해주기

print(result)
========================================================================================

노트 : 
"""


