n = int(input())
dataTuple = tuple(map(int, input().split()))

calList = [0] * n
calList[0] = dataTuple[0]
calList[1] = max(calList[0], dataTuple[1])

for i in range(2, n):
    calList[i] = max(calList[i-1], calList[i-2] + dataTuple[i])

print(calList[n-1])



"""
문제 : p220_개미전사
시간 : 17분

접근 :
calList[0], [1] 값을 먼저 구한 뒤
점화식을 구하여 다이나믹 프로그래밍으로 품


다른 사람 풀이 :
========================================================================================
해설 :
========================================================================================

노트 :
- 다이나믹 프로그래밍의 기본이 되는 문제인데, 접근하는데 오래걸렸음 유사 문제 많이 풀어볼 것
"""