n, m = map(int, input().split())
coinList = []
for i in range(n):
    coinList.append(int(input()))

calList = [10001] * (m + 1)
calList[0] = 0

for i in range(1, m+1):
    for coin in coinList:
        if coin <= i and calList[i-coin] != 10001 and calList[i-coin] + 1 < calList[i]:
            calList[i] = calList[i-coin] + 1

print(-1) if calList[m] == 10001 else print(calList[m])


"""
문제 : p226_효율적인화폐구성
시간 : 13분

접근 :
바텀업으로 1원부터 m원까지 만들 수 있는 가장 적은 화폐의 수를 계산함


다른 사람 풀이 :
========================================================================================
해설 :
for i in range(n):
    for j in range(array[i], m + 1):
반복순서가 n, m 이며
range를 동전 금액부터 시작해서 위에 작성 코드 기준 coin <= i 검사가 필요 없음


# 정수 N, M을 입력 받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
========================================================================================

노트 :
-
"""