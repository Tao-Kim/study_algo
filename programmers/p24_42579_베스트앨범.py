def solution(genres, plays):
    genre_dict = {}

    for i in range(len(genres)):
        if genres[i] in genre_dict:
            genre_dict[genres[i]]["total"] += plays[i]
            genre_dict[genres[i]]["plays"].append((plays[i], i))
        else:
            genre_dict[genres[i]] = {"total": plays[i], "plays": [(plays[i], i)]}

    sorted_genre_list = sorted(genre_dict.items(), key=lambda x: -x[1]['total'])

    answer = []
    for genre in sorted_genre_list:
        genre_plays = genre[1]['plays']
        genre_plays.sort(key=lambda x: (-x[0], x[1]))

        count = 2
        for play in genre_plays:
            count -= 1
            answer.append(play[1])
            if count == 0:
                break

    return answer

"""
문제주소 : https://programmers.co.kr/learn/courses/30/lessons/42579
시간 : 15분


다른 사람 풀이 :
========================================================================================

========================================================================================

노트 :
-
"""