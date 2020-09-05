from collections import deque 

def solution(prices):
    answer = deque()
    max_price = max(prices)
    last_index = len(prices) - 1
    
    down_days = dict(zip(prices, [-1] * (last_index + 1)))
    
    for index in range(len(prices) - 1, -1, -1):
        price = prices[index]
        down_index = down_days[price]
        
        if down_index == -1:
            answer.appendleft(last_index - index)
        else:
            answer.appendleft(down_index - index)
            
        #print(down_days, "price : ",price, "index :", index, "down_index :", down_index, answer)
        
        for down_price in down_days:
            if down_price > price:
                down_days[down_price] = index
    
    
    return list(answer)



"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42584
시간 : xx분

-  효율성 테스트를 통과하지 못함
- 오히려 2중 포문 답변이 테스트를 통과함


다른 사람 풀이 :
========================================================================================
2중 포문
========================================================================================


노트 :
- 
"""