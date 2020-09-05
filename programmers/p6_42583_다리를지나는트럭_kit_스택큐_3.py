def solution(bridge_length, weight, truck_weights):
    trucks_on_bridge = []
    current_time = 1
    current_weight = 0
    
    for truck_weight in truck_weights:
        while current_weight + truck_weight > weight:
            pop_time, pop_weight = trucks_on_bridge.pop(0)
            current_time = pop_time + bridge_length
            current_weight -= pop_weight
            
        if current_weight + truck_weight <= weight:
            current_weight += truck_weight
            trucks_on_bridge.append((current_time, truck_weight))
            current_time += 1
        
            
        for truck_on_bridge in trucks_on_bridge:
            if current_time >= truck_on_bridge[0] + bridge_length:
                current_weight -= truck_on_bridge[1]
                trucks_on_bridge.pop(0)
            
    while trucks_on_bridge:
        pop_time, pop_weight = trucks_on_bridge.pop(0)
        current_time = pop_time + bridge_length
    
    
    return current_time

"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42583
시간 : 23분


다른 사람 풀이 :
========================================================================================

========================================================================================


노트 :
- 
"""