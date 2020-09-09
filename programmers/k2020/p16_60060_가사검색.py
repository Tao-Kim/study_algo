from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    
    #{
    words_reversed = sorted([ ''.join(reversed(word)) for word in words])
    words.sort()
    
    for query in queries:
        print(query)
        print(words)
        print(words_reversed)
        query_length = len(query)
        count = 0
        
        if query[-1] == '?':
            query = query.replace('?','')
            for i in range(bisect_left(words, query), bisect_right(words, query + '{')):
                print(bisect_left(words, query), bisect_right(words, query + '{'), words[i], query_length)
                if len(words[i]) == query_length:
                    count +=1
        else:
            query = ''.join(reversed(query.replace('?', '')))
            for i in range(bisect_left(words_reversed, query), bisect_right(words_reversed, query + '{')):
                print(bisect_left(words_reversed, query), bisect_right(words_reversed, query + '{'), words[i], query_length)
                if len(words[i]) == query_length:
                    count +=1
                    
        answer.append(count)
    
    return answer


    
"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/60060
시간 : 못품 - 30분 풀고 시간 초과
테스트 : 테스트 - 통과 // 정확성 - 5/18 // 효율성  - 2개 시간 초과 

- 5시간 측정 초과해서 다 못품

다른 사람 풀이 :
========================================================================================

========================================================================================

노트 :
- 다시 풀기
"""