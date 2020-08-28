numList = list(map(int, input()))
result = numList[0]

for i in range(1, len(numList)):
    result = max(result + numList[i], result * numList[i])

print(result)



"""
문제 : p312_곱하기 혹은 더하기
시간 : 3분

접근 :
앞에서부터 계산하여 더한 값, 곱한 값 중에 큰 계산을 함

다른 사람 풀이 :
========================================================================================
해설 : 숫자가 0 혹은 1일때만 더하기가 더 크다는 점을 이용함

data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
========================================================================================

노트 :
"""