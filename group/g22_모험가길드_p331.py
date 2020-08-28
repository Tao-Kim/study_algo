n = int(input())
adventureList = sorted(tuple(map(int, input().split())), reverse=True)

current = 0
count = 0

while current < n:
    current = current + adventureList[current]
    if current <= n:
        count += 1

print(count)


"""
문제 : p311_모험가길드
시간 : 8분

접근 :
모험가 n명을 공포도 순으로 정렬하고 그룹을 만들때 가장 큰 공포도 수만큼 모험가를 그룹으로 지정

다른 사람 풀이 :
========================================================================================
해설 : 오름차순으로 정렬해서 count가 >= i가 되면 그룹화 하는 방식

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력
========================================================================================

노트 :
"""