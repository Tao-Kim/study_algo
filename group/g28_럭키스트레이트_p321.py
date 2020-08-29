strNum = input()
mid = len(strNum) // 2

if sum(list(map(int, strNum[:mid]))) == sum(list(map(int, strNum[mid:]))):
    print("LUCKY")
else:
    print("READY")


    
"""
문제 : p321_럭키 스트레이트
시간 : 3분 30초

접근 :
문자열로 입력받고 슬라이싱하여 반나누고 양쪽의 합을 구하여 비교함

다른 사람 풀이 :
========================================================================================
파이썬 map에 바로 sum 가능

n=input()
d=len(n)//2
print("LUCKY"if sum(map(int, n[:d]))==sum(map(int, n[d:]))else"READY")
========================================================================================

노트 : 
- 파이썬 map에 바로 sum 가능 = sum(map(int, ~))
- 파이썬 삼항연산자 = [true_value] if [condition] else [false_value]
"""


