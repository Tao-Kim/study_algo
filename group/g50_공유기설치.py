n, c = map(int, input().split())

house_list = sorted([int(input()) for _ in range(n)])
max_house = max(house_list)
min_house = min(house_list)

check_distance = (max_house - min_house) // (c -1)
findSolution = False

while not findSolution:
    remain_ap = c-1
    last_house = house_list[0]

    for index, house in enumerate(house_list):
        if house - last_house >= check_distance:
            remain_ap -= 1
            last_house = house
            if remain_ap == 0:
                findSolution = True
                break

        if index == n - 1 and remain_ap != 0:
            check_distance -= 1

print(check_distance)

"""
 문제 : p50_공유기설치
 시간 : 23분

 접근 :
 - 이진탐색이 바로 생각나지 않아서 전체 길이를 공유기 갯수로 나누어 가능한 최대 거리의 max를 구한 후 아래로 순차적으로
 답을 찾았는데, 테스트 케이스는 통과하나 시간초과함


 다른 사람 풀이 :
 ========================================================================================

 ========================================================================================

 노트 : 
 - g50 해설 보기
 """
