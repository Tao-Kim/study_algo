n = int(input())
storeItems = tuple(map(int, input().split()))

m = int(input())
requestItems = tuple(map(int, input().split()))

resultList = []

for requestItem in requestItems:
    if requestItem in storeItems:
        print("yes", end=" ")
    else:
        print("no", end=" ")

"""
문제 : p198_부품 찾기
시간 : 5분

접근 :
가게 상품 리스트를 정렬(nlogn)후 이진탐색(logn) 할지
정렬없이 단순탐색(n)으로 할지 고민하다가 우선 후자로 작성했는데 테스트케이스가 있었다면 통과하지 못했을 것 같다.

(1 <= n <= 1,000,000) (1 <= m <= 100,000)
1. T = nlogn + mlogn .... W : 1e6*20 + C .. 1e7 10,000,000
2. T = nm .... W : 1e11 100,000,000,000
"""

def binaryContains(startIndex, endIndex, targetValue):
    if startIndex > endIndex:
        return False
    
    middleIndex = (startIndex + endIndex) // 2
    currentValue = storeItems[middleIndex]
    if currentValue == targetValue:
        return True
    elif currentValue < targetValue:
        return binaryContains(middleIndex + 1, endIndex, targetValue)
    else:
        return binaryContains(startIndex, middleIndex - 1, targetValue)


n = int(input())
storeItems = sorted(tuple(map(int, input().split())))

m = int(input())
requestItems = tuple(map(int, input().split()))

for requestItem in requestItems:
    if binaryContains(0, n-1, requestItem):
        print("yes", end=" ")
    else:
        print("no", end=" ")

"""
문제 : p198_부품 찾기
시간 : 14분

접근 :
상품리스트를 정렬후 이진탐색 활용


다른 사람 풀이 :
========================================================================================
해설 : 반복문으로 만든 이진탐색

# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
        else:
            start = mid + 1
    return None
========================================================================================

노트 :
- 탐색문제 데이터 범위 확인후 이진탐색 적용해야 하는지 여부 먼저 확인하고 문제풀 것
"""