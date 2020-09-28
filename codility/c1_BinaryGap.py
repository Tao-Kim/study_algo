def solution(N):
    # write your code in Python 3.6
    search_list = list(bin(N))[3:]

    count = 0
    gaps = [0]

    for num in search_list:
        if num == '0':
            count += 1
        elif num == '1':
            gaps.append(count)
            count = 0

    return max(gaps)

"""
문제주소 : https://app.codility.com/programmers/lessons/1-iterations/binary_gap/start/
시간 : 11분


다른 사람 풀이 :
========================================================================================

========================================================================================

노트 :
- 
"""