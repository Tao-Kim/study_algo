import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heightList = tuple(map(int, input().split()))


high = max(heightList)
low = min(heightList)

while True:
    mid = (high + low) // 2
    sumOfHeight = 0

    for height in heightList:
        if height > mid:
            sumOfHeight += height - mid
    
    if sumOfHeight == m:
        print(mid)
        break
    elif sumOfHeight > m:
        low = mid + 1
    else:
        high = mid - 1
        
"""
문제 : p201 떡볶이 떡 만들기
시간 : 8분

접근 :




다른 사람 풀이 :
========================================================================================
해설 :
========================================================================================

노트 :

"""