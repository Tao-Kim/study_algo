n = int(input())

num_tuple = tuple(map(int, input().split()))

low = 0
high = len(num_tuple) - 1

while True:
    if low > high:
        print(-1)
        break
        
    mid = (low + high) // 2

    if num_tuple[mid] == mid:
        print(mid)
        break
    elif num_tuple[mid] < mid:
        low = mid + 1
    else:
        high = mid - 1


    """
    문제 : p368_고정점 찾기
    시간 : 3분

    접근 :
    - 인덱스가 커지면 값도 함께 커지고 작아지면 함께 작아지는 특징을 이용한 이진탐색


    다른 사람 풀이 :
    ========================================================================================

    ========================================================================================

    노트 : 
    - 
    """
