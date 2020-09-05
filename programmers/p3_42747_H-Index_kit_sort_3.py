def solution(citations):
    citations.sort(reverse=True)
    
    count = 0
    for citation in citations:        
        if citation >= count + 1:
            count += 1
        else:
            break
    
    return count

"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42747
시간 : 11분


다른 사람 풀이 :
========================================================================================
1. enumerate의 인덱스 활용

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
========================================================================================


노트 :
- enumerate의 인덱스 지정방법 찾아보기
- p3 다른 사람 풀이1 복습
"""