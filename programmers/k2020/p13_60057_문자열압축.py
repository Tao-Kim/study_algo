def solution(s):
    s_length = len(s)
    if s_length == 1:
        return 1
    
    max_cut_length = s_length // 2
    
    min_length = 1001
    
    for i in range(1, max_cut_length+1):
        count = 0
        cut_list = []
        s_temp = ''
        
        for char in s:
            s_temp += char
            count += 1
            
            if count == i:
                cut_list.append(s_temp)
                count = 0
                s_temp = ''
        
        if s_temp:
            cut_list.append(s_temp)
        
        
        result = ''
        same_count = 1
        previous_cut = cut_list[0]
        
        for cut in cut_list[1:]:
            if cut == previous_cut:
                same_count += 1
            else:
                if same_count == 1:
                    result += previous_cut
                else:
                    result += str(same_count) + previous_cut
                previous_cut = cut
                same_count = 1
        
        if same_count != 1:
            result += str(same_count) + previous_cut
        else:
            result += previous_cut
            
        min_length = min(min_length, len(result))
                
    
    return min_length

"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/60057
시간 : 30:12
테스트 : 28/28

- 모든 경우를 코드로 풀어 구현함
- 코드 가독성이 심각하게 떨어짐
- 파이썬 함수들을 이용하면 더 깔끔하게 풀 수 있을거 같음

다른 사람 풀이 :
========================================================================================

========================================================================================

노트 :
- p13 다른 사람 풀이 찾아보기
"""