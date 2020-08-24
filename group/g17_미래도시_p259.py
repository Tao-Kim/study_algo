INFINITY = 987654321
n, m = map(int, input().split())

arr = [[INFINITY] * (n + 1) for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if arr[j][k] > arr[j][i] + arr[i][k]:
                arr[j][k] = arr[j][i] + arr[i][k]

x, k = map(int, input().split())

result = arr[1][k] + arr[k][x]
if result >= INFINITY:
    print(-1)
else:
    print(result)


"""
문제 : p259_미래도시
시간 : 18분

접근 :
플루이드 워셜 알고리즘으로 품
1, k // k, x 두개를 다익스트라로 풀어도 될듯함


다른 사람 풀이 :
========================================================================================
해설 :
========================================================================================

노트 :
- 
"""