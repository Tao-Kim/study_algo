import sys
input = sys.stdin.readline

n, m = map(int, input().split())
itemList = tuple(map(int, input().split()))

def binarySlice(minHeight, maxHeight):
    middleHeight = (minHeight + maxHeight) // 2

    sumOfSlicedHeight = 0
    for item in itemList:
        if item - middleHeight > 0:
            sumOfSlicedHeight += item - middleHeight

    if sumOfSlicedHeight == m:
        return middleHeight
    elif sumOfSlicedHeight > m:
        return binarySlice(middleHeight + 1, maxHeight)
    else:
        return binarySlice(minHeight, middleHeight - 1)


print(binarySlice(min(itemList), max(itemList)))

"""
문제 : p201 떡볶이 떡 만들기
시간 : 측정안함

접근 :
처음에 문제를 잘못이해해서 엉뚱하게 접근함
문제에서 요구하는건 고정된 떡들의 윗부분을 자르고 위에 잘린 떡들의 합이 m이 되는 방식이므로
자르는 높이가 높아질수록 떡의 양이 적어지고 반대는 많아지는 점을 이용해서 이진 탐색이 가능함



다른 사람 풀이 :
========================================================================================
해설 :
========================================================================================

노트 :
- 파라메트릭 서치 유형 접근법 고려하기
- 문제 조건이 다소 부족한 것 같음
"""