def solution(phone_book):
    check_dict = dict()
    
    phone_book.sort(key=lambda x : -len(x))
    
    for phone in phone_book:
        if check_dict.get(phone):
            return False
        
        str_temp = ''
        for char in phone:
            str_temp += char
            check_dict[str_temp] = True
    
    
    return True

"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42577
시간 : 12분


다른 사람 풀이 :
========================================================================================
sort의 문자열 정렬 특징을 이용
119, 1195 순으로 정렬 됨

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
========================================================================================


노트 :
- 파이썬 자료구조 메소드 복습
"""