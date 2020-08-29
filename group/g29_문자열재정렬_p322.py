alphabetList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

inputString = input()
charList = []
sum = 0

for char in inputString:
    if char in alphabetList:
        charList.append(char)
    else:
        sum += int(char)

print(''.join(sorted(charList)) + str(sum))

"""
문제 : p322_문자열 재정렬
시간 : 4분 30초

접근 :
대문자 문자열을 선언하고 입력 문자열의 각 문자가 대문자인지 구별하여 처리함

다른 사람 풀이 :
========================================================================================

========================================================================================

노트 : 
- x.isalpha() ... 파이썬 문자열 조작 복습
- 파이썬 문자열에 정규식 적용하는게 있는지 찾아보기
"""


