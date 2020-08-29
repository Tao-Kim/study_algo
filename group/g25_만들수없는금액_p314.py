n = int(input())
coinList = tuple(map(int, input().split()))

calList = set()
calList.add(0)

for coin in coinList:

    temp = calList.copy()
    for cal in temp:
        calList.add(cal+coin)


for i in range(sum(calList)+1):
    if i not in calList:
        print(i)
        break


"""
문제 : p314_만들 수 없는 금액
시간 : 10분

접근 :
만들 수 있는 전체 금액을 set으로 구하고
만들 수 없는 가장 작은 금액을 선택하는 방식으로 구하였는데
메모리 낭비가 심한 것 같다.

다른 사람 풀이 :
========================================================================================
현 단계에서 target-1 까지는 모두 만들 수 있다는 전제가 생긴다.
즉 target = x 일때는 x 동전 자체를 넣으면 되고
target > x 일때는 x + (target-1중 한 값) 으로 만들 수 있다는 의미
한번 보고 이 로직을 파악할 수 있을ㄲ ㅏ..?


n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)
========================================================================================

노트 : 복습 g25
"""


