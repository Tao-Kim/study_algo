from itertools import combinations

def make_all_case_index_list(relation):
    all_case_index_list = []
    len(relation)
    column_index_list = [i for i in range(len(relation[0]))]

    for i in range(1, len(relation[0])+1):
        all_case_index_list.extend(combinations(column_index_list, i))

    return  all_case_index_list

def solution(relation):
    candidate_keys = []
    all_case_index_list = make_all_case_index_list(relation)

    for case in all_case_index_list:
        is_minimality = True
        for candidate_key in candidate_keys:
            if set(candidate_key).issubset(set(case)):
                is_minimality = False

        if is_minimality:
            case_relation = [[relation[index][column] for column in case] for index in range(len(relation))]
            is_unique = True
            for tuple in case_relation:
                if case_relation.count(tuple) > 1:
                    is_unique = False
            if is_unique:
                candidate_keys.append(case)

    answer = len(candidate_keys)
    return answer

"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42890
시간 : 29:59
테스트 : 28/28

- 
다른 사람 풀이 :
========================================================================================

========================================================================================

노트 :
-
"""